# AGI_Startup
Startup of an AGI using Chat GPT4 and function / subroutine calling

#Requirements

Python 3.11.4 (lower versions may be ok)

download and install Git

# INSTALLATION (Windows)

on a command prompt type following commands:
   ```bash
   git clone https://github.com/alperinugur/AGI_Startup

   cd AGI_Startup

   python -m venv venv

   venv\Scripts\activate.bat

   pip3 install -r requirements.txt

   ren .keys.json.template .keys.json

   notepad .keys.json
  ```

Change the values in .keys.json file to your API KEYS

to get an "weatherAPIKey" use the instructions here :    https://www.weatherapi.com/signup.aspx

to get an "OPENAI_API_KEY" for ChatGPT, create an account here :    [https://platform.openai.com/playground ](https://platform.openai.com/account/api-keys)
and then create a new secret key. Copy that key, and paste it inside the notepad's OPENAI_API_KEY value. 
This way, you can track how much you spend on this code.

Save / Overwrite your .keys.json file

when finished, type the below to run:
   ```bash
   python AGI_Startup.py
   ```

# Hints
Rename keys.json.template as keys.json and put your API keys there.

Follow the below links to create API keys if you don't have:

OPEN AI API KEY:  https://platform.openai.com/account/api-keys

WeatherAPI API KEY: https://www.weatherapi.com/signup.aspx

# Features

The code allows you to chat with the ChatGPT3 / ChatGPT4 and call functions if chatGPT finds it necessary.

This is a simple demonstration of what the function calling in ChatGPT is..

# What it does

User prompt asks for a user input.
The input is sent to ChatGPT (function call enabled)
If ChatGPT decides it has to look on the date/time or weather in somewhere, it calls the matching function. The response of the matching function is sent to ChatGPT again, to make an reasonable reply on the content.

If ChatGPT decides not to use any function, the regular response is returned (printed on the terminal window) to user.

# IDEAS

Anyone who wish to contribute is welcome. My privilidges are as follows:

  * Remember the complete chat before, so the chat is consistent / DONE
  * Make a function to create text files, to store what actions were performed (STORE_MEMORY) / DONE
  * Make a function to read text files, to remember what actions were performed (RECALL_MEMORY) / DONE
  * Make a function to write / read file, on the users request (i.e. If user prompts "Create a c# code that surfs a webpage and get headers in the webpage, the function will create a file named XXXXX.cs which is a c# / DONE for Python


# THANKS 
