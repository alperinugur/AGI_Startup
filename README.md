# ChatGPT Function Executor

This project is an application that leverages the OpenAI GPT-3.5 or GPT-4 models to execute a list of predefined functions based on user input. The script reads an API key from a JSON file and uses that to authenticate with the OpenAI API. Also if you want to use Weather Data, or let the ChatGPT do Google Searches, follow below for the websites you can get them for free!

This project serves as a conversational interface that can execute a list of predefined functions, powered by the advanced AI capabilities of OpenAI's GPT-3.5 or GPT-4 models. Leveraging a chat-based format, the script dynamically reads user input and maps it to a relevant function to perform the requested operation. To facilitate secure interactions with OpenAI's API, the script reads an API key from a local JSON file for authentication. This application showcases an innovative way to harness the power of AI, creating a seamless blend of human-computer interaction and automated task execution. From fetching the current weather, writing to a file, reading from a file, making google searches, to running Python code, this script demonstrates a fascinating use case of AI in automating task-oriented conversations.


## Prerequisites

Before you begin, ensure you have met the following requirements:
* You have installed Python 3.6 or later.
* You have a basic understanding of Python programming language.
* You have obtained an API key from OpenAI. (Mandatory!)  <http://api.weatherapi.com>
* You have obtained an API key from weatherapi. (optional) <http://api.weatherapi.com>
* You have obtained an API key from google. (if you want to use the google search function) <https://console.cloud.google.com/apis/credentials>
* You have obtained an Search Engine ID from google. (if you want to use the google search function) <https://programmablesearchengine.google.com>

## Getting Started

THE CODE IS ABLE TO RUN PYTHON CODES on the "./codes" folder if you ask it to. So be careful and use it on your own risk!

First, clone the repository to your local machine:

```
git clone https://github.com/alperinugur/AGI_Startup
```

After you clone the repository, navigate to the project directory:

```
cd AGI_Startup
```

Create an environment (Recommended), and enable it:

```
python -m venv venv
venv\scripts\activate.bat
```

Install Requirements
```
(venv) C:\Users\Name\AGI_Startup> pip install -r requirements.txt
```

## Configuration

You must provide your OpenAI API key to be able to interact with the ChatGPT models. You should save your API key in a JSON file named '.keys.json'. It should be structured as follows:

```json
{
    "weatherAPIKey" : "GetYoutWeatherAPIkey_from http://api.weatherapi.com",
    "OPENAI_API_KEY" : "Your_openai_API_key from https://platform.openai.com/account/api-keys",
    "GOOGLE_API_KEY" : "Your Google API Key from https://console.cloud.google.com/apis/credentials",
    "GOOGLE_SEARCH_ENGINE_ID" : "Google Search Engine ID From https://programmablesearchengine.google.com"
}
```

Please replace "your_openai_api_key" with your actual API key. 

There is a .keys.json.template file, you can rename it to ".keys.json" and replace your keys with placeholders.

To run the program, you can use Visual Studio Code (or any other software), or after enabling the env (venv):
```
venv\scripts\activate.bat
python.exe AGI_Startup.py
```

## Functions

The available function list consists of:

- `get_weather`
- `get_current_time`
- `write_to_file`
- `write_python_code_to_file`
- `read_from_file`
- `show_image`
- `run_python_code`
- `search_in_google`    ** Newly added feature. Searches google, and gets the first page results..

Each function is defined in `all_functions.py` file, and you can easily create your own functions.

## Usage

To start using the application, run:

```
python3 AGI_Startup.py
```

You will see an input prompt where you can enter your message or command. Available commands include:

- `cls`: Clears the console.
- `save`: Saves the current conversation to 'messages.json'.
- `load`: Loads the conversation history from 'messages.json'.
- `new`: Clears the current conversation in memory.
- `exit`: Exits the application. You'll be prompted to save the current conversation before exiting.
- `dump`: Prints out the current conversation.

The application will prompt you for input, which will be processed by the ChatGPT model to select the appropriate function from the available list to execute.

## Error Handling

The application also contains error handling for cases where the context length is exceeded, which could occur if the conversation history becomes too large.

## Contributing to ChatGPT Function Executor

To contribute to ChatGPT Function Executor, follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## License

This project uses the following license: [MIT License](https://opensource.org/licenses/MIT).
