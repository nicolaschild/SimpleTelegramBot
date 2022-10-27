import requests
"""
Use this script to send messages from your telegram bot!
All that is required is the chat id, api key, and a message of your choosing
*Great for Zapier*
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
