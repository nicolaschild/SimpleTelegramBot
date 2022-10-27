import requests
"""
Hello world!
You sick and tired of looking for a simple way to just send a Telegram Message with the Bot API?
Don't want to install a package? Awesome, me neither!
"""

message = f"custom message here!"
apiKey = "" #Insert your API key here
chatId = "" #Insert the target chat ID here, to find this, reference telebot.py
baseLink = f"https://api.telegram.org/bot{apiKey}/sendMessage?chat_id={chatId}&text={message}"
header = {
    "Accept" : "application/json",
    "X-API-KEY" : "" #APIK here (probably not necessary)
}
testBot = (requests.get(baseLink, headers=header)).json()