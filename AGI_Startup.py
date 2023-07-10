import openai
import json
import sys

global  ChatGPTModelToUse

with open('.keys.json', 'r') as f:
    params = json.load(f)
    openai.api_key = params['OPENAI_API_KEY']

ChatGPTModelToUse = "gpt-3.5-turbo-0613"    # put "gpt-4-0613" to make use of ChatGPT4   

global messages

from all_functions import *

def function_needed(myin):
    global messages
    if messages == []:
        messages = ([{"role": "user", "content": myin}])
    else:
        messages.append({"role": "user", "content": myin})

    function_selector_fn = [
            {
                "name": "function_selector",
                "description": """Gets the function_name from the available function list only: 
                                get_weather
                                get_current_time 
                                write_to_file
                                write_python_code_to_file
                                read_from_file
                                show_image
                                run_python_code
                                """,
                "parameters": {
                    "type": "object",
                    "properties": {
                        "function_name": {
                            "type": "string",
                            "description": "Name of the function to use",
                        },
                    },
                    "required": ["function_name"],
                },
            }

        ]
    try:
        response = openai.ChatCompletion.create(
            model=ChatGPTModelToUse,  
            messages=messages,
            functions=function_selector_fn,
            function_call="auto",  # auto is default, but we'll be explicit
        )
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        exception_code = exc_obj.code
        print("Exception code:", exception_code)
        if exception_code == "context_length_exceeded":
            print (f"OLD:\n{messages}")
            messages= messages[2:]
            messages = messages[:-1]
            print (f"NEW:\n{messages}")
            return ("OPENAI_ERROR_TOO_MUCH_CONV")
        else:
            messages = messages[:-1]
            return ('ERROR CONNECTING\n')

    updatetokens(response) 

    i=0
    for resps in response["choices"]:
        i += 1
        if i >1: print (f'Response {i} :  \n{resps["message"]}\n\n')

    response_message = response["choices"][0]["message"]
    fn = response_message.get("function_call")

    if response_message.get("function_call"):
        fn = response_message.get("function_call")
        #funcName=response_message["function_call"]["name"]
        try:
            funcArgs= json.loads(response_message["function_call"]["arguments"])
        except:
            funcArgs = fn["arguments"]

        try:
            nfuncName = funcArgs['function_name']
        except:
            nfuncName = fn['name']

        print (f'👿 ChatGPT decided to Function to be used: {nfuncName}\n')            
        available_functions = {
                    "get_weather": get_weather,
                    "get_current_time" : get_current_time,
                    "write_python_code_to_file" : write_python_code_to_file,
                    "write_to_file" : write_to_file,
                    "read_from_file" : read_from_file,
                    "show_image":show_image,
                    "run_python_code":run_python_code,
                }
        if nfuncName not in available_functions:
            return (f'No corresponding function: {nfuncName}')
        function_to_call = available_functions[nfuncName]
        function_interior = get_function_to_use(nfuncName)
        function_response = function_to_call(
            myin=messages,
            function_args=[function_interior],
        )
        messages.append ({"role": "assistant", "content": function_response})
        return(function_response)

    else:
        messages.append ({"role": "assistant", "content": response_message["content"]})
        return (response_message["content"])

def initialize():
    global messages
    cls()
    try:
        with open('messages.json', 'r',encoding='utf-8') as openfile:
            messages = json.load(openfile)
    except:
        dt=get_current_time()
        messages= ([{"role": "user", "content": f'Now is {dt}'}])
        messages.append ({"role": "assistant", "content": f'Ok. It is {dt}'})
    print(f'👻 Loaded {len(messages)} messages from history. Type dump to see messages.')

def clearmemory():
    global messages
    cls()
    dt=get_current_time()
    messages= ([{"role": "user", "content": f'Now is {dt}'}])
    messages.append ({"role": "assistant", "content": f'Ok. It is {dt}'})
    print('\nConversations Cleared From Memory.\nType SAVE if you want to clear from Disk.')


if __name__ == '__main__':
    initialize()
    while True:
        myin = input ("😎 User : ")
        if len(myin)<3:
            exit()
        elif myin.lower() == "cls": 
            cls()
        elif myin.lower() == "save":
            with open("messages.json", "w",encoding='utf-8') as outfile:
                json.dump(messages, outfile)
        elif myin.lower() == "load":
            with open('messages.json', 'r',encoding='utf-8') as openfile:
                messages = json.load(openfile)
        elif myin.lower() == "new":
            clearmemory()
        elif myin.lower() == "exit":
            exitSave = input ("😎 Save Conversation for next chat?  (Y for Yes) :  ")
            if exitSave.lower() in {'y','yes'}:
                with open("messages.json", "w",encoding='utf-8') as outfile:
                    json.dump(messages, outfile)
                print('👻 AI   : Conversation Saved and will be automatically loaded in next start')
            else:
                print('👿 AI   : Conversation Discarded')

            exit()
        elif myin.lower() =="dump":
            try:
                for message in messages:
                    print (f"{message['role'].ljust(14)}: {message['content']}")
            except:
                print (messages)

        else:
            # If the message is not a direct command like cls / save / load / new / dump then let's ask ChatGPT
            while True:
                getresult = function_needed(myin)
                if getresult != "OPENAI_ERROR_TOO_MUCH_CONV":   # if the input is not too much, then the result is retrieved below
                    print(f'👻 AI   : {getresult}')
                    break

