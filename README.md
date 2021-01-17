# Humanoid Chatbot

A telegram bot for getting answers to a lot of frequently asked questions for freshers coming to IIT Mandi.

## Technologies Used

* Flask
* ngrok
* python-telegram-bot
* Dialogflow
* APIs: Firebase, Google Maps, Stack Exchange

## How to run locally

1. Clone the repository.
2. Create an evironment using `venv`.
3. Install required dependencies using pip from `requirements.txt`.
4. Get a telegram bot token from the [BotFather](https://t.me/botfather) bot at telegram.
5. Setup a proxy server using [ngrok](https://ngrok.com/download) and set the port number to be the same as chosen in your Flask server(only few ports are accepted by telegram eg-8443). The command for that is: `./ngrok http 8443`.
6. Run the ngrok server and copy the forwarding URL of the form https://*randomseq*.ngrok.io/. This will be the URL for our webhook.
7. Set the bot token and URL for webhook as environment variables in the .env file as follows: `TOKEN=<YOUR_TOKEN>` and `url_for_webhook=<URL>`.
8. Run the bot.py file. The bot will read and print logs of information like intents detected and text extracted from the voice message.

## Features

Humanoid can answer various queries of freshers related to:

* campus
* hostels, mess, and canteens
* academics, and curriculum
* clubs, societies, and fests

..and a lot of other amazing things at IIT Mandi. Also, it provides some additional features like:

* Speech recognition for interaction.
* Providing documents and other resources related to admission and academics.
* Suggesting ideal travelling routes to the campus from the user's location.
* Searching for posts on stackoverflow's websites for doubts related to programming.

## How to contribute

Clone the repo and feel free to send any Pull Requests that you feel to be constructive.

## Team Members

[Tushar Goyal](https://github.com/tushargoyal22), [Karan Doshi](https://github.com/karansdoshi), [Prakhar Uniyal](https://github.com/PrakharUniyal)
