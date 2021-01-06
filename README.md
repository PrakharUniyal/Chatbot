# Chatbot



## Local Setup

1. Fork the repository.

2. Clone the forked repository.

```console
git clone https://github.com/PrakharUniyal/Chatbot.git
```

3. Enter the repository.

```console
cd Chatbot
```

4. Create a python virtual environment with ```python=python3```.

```console
python3 -m venv myvenv
```

5. Activate the virtual environment.

```console
source myvenv/bin/activate
```


6. Install required python packages from requirements.txt.

```console
pip install -r requirements.txt
```

7. Generate Public URL for Webhook using ngrok

 - Run ngrok from command line (from the place where ngrok executable is stored)

```console
./ngrok http 8443
```
Copy the HTTPS Forwarding URL and Replace in [Code](https://github.com/PrakharUniyal/Chatbot/blob/main/bot.py#L82)


8. Run application

```console
python3 bot.py
```