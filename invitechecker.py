import requests
import random
import json
import threading
import urllib3
from pystyle import Write, System, Colors, Colorate, Anime
from colorama import Fore as f
import datetime
import requests
import random
import time
import threading
import httpx
from capmonster_python import HCaptchaTask
import time, re
from requests import Session
import string
from fake_useragent import UserAgent
from colorama import Fore as f
from pystyle import Write, System, Colors, Colorate, Anime
from colorama import Fore as f
from colorama import Fore
import os, random, string, time, json, sys, ctypes
import datetime
from json        import dumps


urllib3.disable_warnings()

def get_time_rn():
    date = datetime.datetime.now()
    hour = date.hour
    minute = date.minute
    second = date.second
    timee = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
    return timee


def count_invites():
    # Open invites.txt and count the number of lines
    with open('invites.txt', 'r') as invites_file:
        num_invites = sum(1 for _ in invites_file)
    return num_invites

def get_discord_invite_info():
    num_invites = count_invites()
    print("Loadet", num_invites, "Invites")
    time_rn = get_time_rn()
    # Read proxies from the file
    with open('proxies.txt') as f:
        proxies_list = f.read().splitlines()

    # Read invite codes from the file
    with open('invites.txt', 'r') as invites_file:
        invite_codes = invites_file.readlines()


    for _ in range(num_invites):
        # Choose a random invite code and proxy for each request
        invite_code = random.choice(invite_codes).strip()
        proxy = random.choice(proxies_list)

        try:
            response = requests.get(f'https://discord.com/api/v9/invites/{invite_code}?with_counts=true',
                                    verify=False,
                                    proxies={'http': 'http://' + proxy, 'https': 'http://' + proxy})



            if response.status_code == 200:
                data = response.json()
                offline = data.get('approximate_presence_count')
                online = data.get('approximate_member_count')
 
                print(f"{Fore.MAGENTA}[{time_rn}] [{Fore.GREEN}{invite_code}{Fore.MAGENTA}]{Fore.WHITE} Online members[{online}] Offline[{offline}] Statuscode[{response.status_code}] \u2705")
                with open('working.txt', 'a') as works_file:
                    works_file.write(invite_code + '\n')
                with open('capture.txt', 'a') as capture_file:
                    capture_file.write(f"{invite_code} Online {online} Offline {offline}\n")
                
            elif response.status_code == 404:
                print(f"{Fore.MAGENTA}[{time_rn}] [{Fore.RED}{invite_code}{Fore.MAGENTA}]{Fore.WHITE} Invalid Invitecode Statuscode[{response.status_code}] \u2705")
                with open('notworking.txt', 'a') as notworking_file:
                    notworking_file.write(invite_code + '\n')
            elif response.status_code == 429:
                print(f"{Fore.MAGENTA}[{time_rn}] [{Fore.RED}Discord{Fore.MAGENTA}]{Fore.WHITE} Ratelimited {response.status_code} Statuscode[{response.status_code}] \u2705")
            else:
                print("Status Code:", response.status_code)
        except Exception as e:
            print("Error occurred:", e)



# Create threads and start them
threads = []
for _ in range(1):
    thread = threading.Thread(target=get_discord_invite_info)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
