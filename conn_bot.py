# python3 script for sending message to TELEGRAM about connect or disconnect AllStarLink node
# usage:
# python3 conn_bot.py 0 12345 67898
#
#
#
# for automatic usage with AllStarLink you need
# edit /etc/asterisk/rpt.conf
# and add there command like
# connpgm = python3 </full/path/to>/aslnotify/conn_bot.py 1
# discpgm = python3 </full/path/to>/aslnotify/conn_bot.py 0
#


# Import Libraries
import requests
import sys
from datetime import datetime, date, time, timedelta

# Fill arguments
mynode = sys.argv[2]
theirnode = sys.argv[3]
connstatus = sys.argv[1]

# Define function for sending message
def send_msg(text):
   token = "your-telegram-bot-token"
   chat_id = "your-chat-id"
   url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
   results = requests.get(url_req)
   #print(results.json())

# do some logic for create a message
status = "ASL Node " + mynode

if int(connstatus) == 1:
    status = status + " connected to "
else:
   status = status + " disconnected from "

now = datetime.now()

status = status + theirnode + " at " + now.strftime("%H:%M:%S")

# send message with status
send_msg(status)
