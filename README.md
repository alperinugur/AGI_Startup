# AGI_Startup
Startup of an AGI using Chat GPT4 and function / subroutine calling


# Installation
Rename keys.json.template as keys.json and put your API keys there.

Follow the below links to create API keys if you don't have:

OPEN AI API KEY:  https://platform.openai.com/account/api-keys

WeatherAPI API KEY: https://www.weatherapi.com/signup.aspx

# Features

The code allows you to chat with the ChatGPT3 / ChatGPT4 and call functions, if chatGPT finds it necessary.

This is a simple demonstration of what the function calling in ChatGPT is..

# What it does

User prompt asks for a user input.
The input is sent to ChatGPT (function call enabled)
If ChatGPT decides it has to look on the date/time or weather in somewhere, it calls the matching function. The response of the matching function is sent to ChatGPT again, to make an reasonable reply on the content.

If ChatGPT decides not to use any function, the regular response is returned (printed on the terminal window) to user.

# IDEAS

Anyone who wish to contribute is welcome. My privilidges are as follows:

  * Remember the complete chat before, so the chat is consistent
  * Make a function to create text files, to store what actions were performed (STORE_MEMORY)
  * Make a function to read text files, to remember what actions were performed (RECALL_MEMORY)
  * Make a function to write / read file, on the users request (i.e. If user prompts "Create a c# code that surfs a webpage and get headers in the webpage, the function will create a file named XXXXX.cs which is a c#


# THANKS 
