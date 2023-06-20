import openai
import json
import time
import requests
import datetime

global weatherAPIKey

with open('.keys.json', 'r') as f:
    paramsNew = json.load(f)
    openai.api_key = paramsNew['OPENAI_API_KEY']
    weatherAPIKey = paramsNew['weatherAPIKey']


# Example dummy function hard coded to return the same weather
# In production, this could be your backend API or an external API

def get_weather(location, unit="celcius"):
    api_key = weatherAPIKey
    base_url = "http://api.weatherapi.com/v1/current.json"
    ReplyText = get_weather_replies()

    # Create the parameters for the request
    params = {
        'key': api_key,
        'q': location
    }

    tempval = "Unable to get weather info.."

    # Make the request
    response = requests.get(base_url, params=params)

    # Parse the response
    if response.status_code == 200:
        data = response.json()
        
        weathertemp = data['current']['temp_c']
        weathercity = data['location']['name'] + ", " + data['location']['country']
        weatherstat =  data['current']['condition']['text']
        weatherwind =  data['current']['wind_kph']
        weatherfeel =  data['current']['feelslike_c']
        if unit == "fahrenheit":
            weathertemp = data['current']['temp_f']
            weatherfeel =  data['current']['feelslike_f']


        tempval = f"{ReplyText['curw']} {weathercity} \n\n"
        if unit == "fahrenheit":
            tempval = tempval + f"{ReplyText['temp']} {weathertemp}°F\n"
            tempval = tempval + (f"{ReplyText['feel']} {weatherfeel}°F\n")
        else:
            tempval = tempval + f"{ReplyText['temp']} {weathertemp}°C\n"
            tempval = tempval + (f"{ReplyText['feel']} {weatherfeel}°C\n")

        tempval = tempval + (f"{ReplyText['stat']} {weatherstat}\n")
        tempval = tempval + (f"{ReplyText['wind']} {weatherwind}{ReplyText['unit']} \n")
            
    return (tempval)

def get_weather_replies():
    return {
		"errCon": "Error getting weather info for",
		"errcity": "Error getting weather info. Please specify city",
		"errUnkn": "Error getting weather info (B)",
		"curw": "Current weather status in ",
		"temp": "Temperature: ",
		"feel": "Feels like : ",
		"stat": "Status     : ",
		"wind": "Wind       : ",
		"unit": " kmph"
    }

def get_current_time():
    nowtime = datetime.datetime.now()
    #print (nowtime)
    return (nowtime)


def run_conversation(myin):
    # Step 1: send the conversation and available functions to GPT
    messages = [{"role": "user", "content": myin}]
    functions = [
        {
            "name": "get_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and country name, e.g. Istanbul, Turkey",
                    },
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                },
                "required": ["location"],
            },
        },
        {
        "name": "get_current_time",
        "description": "Get the current time",
        "parameters": {
            "type": "object",
            "properties": {
            "location": {
                "type":"string",
                "description":"Location for time, e.g. Istanbul",
        },
            },
            "required" : [],
            }
        }

    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        functions=functions,
        function_call="auto",  # auto is default, but we'll be explicit
    )
    response_message = response["choices"][0]["message"]

    # Step 2: check if GPT wanted to call a function
    if response_message.get("function_call"):
        # Step 3: call the function
        # Note: the JSON response may not always be valid; be sure to handle errors
        available_functions = {
            "get_weather": get_weather,
            "get_current_time" : get_current_time,
        }  # only one function in this example, but you can have multiple
        function_name = response_message["function_call"]["name"]
        function_to_call = available_functions[function_name]
        function_args = json.loads(response_message["function_call"]["arguments"])

        if function_name== "get_weather":
            function_response = function_to_call(
                location=function_args.get("location"),
                unit=function_args.get("unit"),
            )

        elif function_name == "get_current_time":
            function_response = str(function_to_call())
        else:
            exit(1)

        #print (f'Function Response: {function_response}\n\n')
        # Step 4: send the info on the function call and function response to GPT
        messages.append(response_message)  # extend conversation with assistant's reply
        messages.append(
            {
                "role": "function",
                "name": function_name,
                "content": function_response,
            }
        )  # extend conversation with function response
        time.sleep(1)
        second_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages,
        )  # get a new response from GPT where it can see the function response
        return (second_response["choices"][0]["message"]["content"])
    else:
        return (response_message["content"])

while True:
    myin = input ("User: ")
    print(run_conversation(myin))
