try:
    import os
except ImportError:
    os.system('pip install os')

try:
    import logging
except ImportError:
    os.system('pip install logging')

try:
    import time
except ImportError:
    os.system('pip install time')

try:
    import pathlib
except ImportError:
    os.system('pip install pathlib')

try:
    import colorama
except ImportError:
    os.system('pip install colorama')

try:
    import selenium
except ImportError:
    os.system('pip install selenium')

try:
    import threading
except ImportError:
    os.system('pip install threading')

try:
    import firebase_admin
except ImportError:
    os.system('pip install firebase_admin')

try:
    import dhooks
except ImportError:
    os.system('pip install dhooks')

try:
    import random
except ImportError:
    os.system('pip install random')

try:
    import requests
except ImportError:
    os.system('pip install requests')

try:
    import socket
except ImportError:
    os.system('pip install socket')

try:
    import json
except ImportError:
    os.system('pip install json')

# Imports
import os
import logging
import sys
from time import sleep
from pathlib import Path
import colorama
from colorama import init
from colorama import Fore, Back, Style
from selenium import webdriver
import threading
from firebase_admin import credentials, initialize_app, storage
from dhooks import Webhook, Embed
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import requests
import socket
from time import time
import json

# Variables
testmode = False
productionmode = True
debug = False
version = "1.2.1"
REQUEST_URL = 'https://api16-core-c-useast1a.tiktokv.com/aweme/v1/aweme/stats/?ac=WIFI&op_region=SE&app_skin=white&'

# Colorama Init
init()

# More Things
link = "https://www.tiktok.com/@all_thingsf1/video/6991814608394718465?sender_device=pc&sender_web_id=6992187022561035778&is_from_webapp=v1&is_copy_url=0"

ipinfo = "http://ipinfo.io/json"
data = requests.get(ipinfo)

if data.ok:
    pass
else:
    sys.exit()

data = requests.get(ipinfo).json()

ip = data['ip']
org = data['org']
city = data['city']
country = data['country']
region = data['region']

if testmode == True:
    print(ip)
    print(org)
    print(city)
    print(country)
    print(region)
    print(socket.gethostname())
else:
    pass

r = requests.get(f"https://extreme-ip-lookup.com/json/{ip}")

tiktokapi = "https://LUClP-Backend.lucaastohmeh.repl.co/api/v1/resources/update/tiktokdata"
tiktokdata = requests.get(tiktokapi).json()

clickviews = tiktokdata['clickviews']
linkinput = tiktokdata['linkinput']
firstsubmit = tiktokdata['firstsubmit']
secondsubmit = tiktokdata['secondsubmit']

firebasedata = "https://LUClP-Backend.lucaastohmeh.repl.co/api/v1/resources/update/firebase"
firebaseapi = requests.get(firebasedata).json()

# Checks Module
def checks():
    sleep(2)

    os.system('cls')

    os.system('title LoelP Tools, Current version = V1.2')

    file = Path("main.txt")

    if file.is_file():
        pass
    else:
        file1 = open(r"main.txt", "w+")
        username = input(
            str("Please enter a unique username, this will be used to assist us with any issues you have: "))
        file1.write(username)
        file1.close()

    # Logging Setup
    file1 = open("main.txt", "r+")

    user = file1.read()
    file1.close()

    logging.basicConfig(filename=f'logs/{user}.log', level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logger = logging.getLogger(__name__)



    # Checking version
    textcheckingversion = rf"""
| *    *    .     *     *    .      *      __    __  __________________ *       *    .     *     *    .      *    *   |
|  .    .       *       *   .    *        / /   / / / / ____/  _/ __  /     .    .       *       *   .    *  .  *  .  |
| *     .    *   .     *    .    *   .   / /   / / / / /    / // /_/ /   *     .    *   .     *    .    *    .   *    |
|     .    *     *   .    *    .     *  / /___/ /_/ / /____/ // ____/  *     .    *     *   .    *    .     *   .  .  |
| *   .   *       .       *       *    /_____/\____/\____/___/_/      *   .   *       .       *       *     .  *    . |
|*       *    .     *     *    .    *  . [Checking LUClP Version] *       *    .     *     *    .      *   .     *  . |
|    *       *    .     *     *    .      *    *       *    .     *     *    .      *    .     *    .    *     . *    |
| .   *  .    *    *   .   *     *     *    .   *    *    .    .   *     *   .    *   .   *    .   *   .   *    *   * |
|    .   *    .    *   *   .   *    .    .   *    .     *    *    .   *    .    *    .    *   .     *    .    *    *  |
| *    *    .     *      *     .   *   .   .    *    *    .    *    .    *     *     *    .      .    .    *    .     |
|   .    .     *     .      *     .    *    *    .    .    *     *     *    .     *    .     *     .    *    .     *  |
|    *       *    .     *     *    .      *    *       *    .     *     *    .      *    .     *    .    *     . *    |
| .   *  .    *    *   .   *     *     *    .   *    *    .    .   *     *   .    *   .   *    .   *   .   *    *   * |
|    .   *    .    *   *   .   *    .    .   *    .     *    *    .   *    .    *    .    *   .     *    .    *    *  |
| *    *    .     *      *     .   *   .   .    *    *    .    *    .    *     *     *    .      .    .    *    .     |
|   .    .     *     .      *     .    *    *    .    .    *     *     *    .     *    .     *     .    *    .     *  |
"""
    # Printing
    bad_colors = ['CYAN', 'WHITE']
    codes = vars(colorama.Fore)
    colors = [codes[color] for color in codes if color in bad_colors]
    colored_chars = [random.choice(colors) + char for char in textcheckingversion]

    print(''.join(colored_chars))

    # Checking version
    response = requests.get("https://lowidenticalvertex.lucaastohmeh.repl.co/api/v1/resources/update/all")
    response.headers.get("Content-Type")

    response.json()
    latestversion = response.json()["latestversion"]

    if latestversion == version:
        pass
    else:
        sleep(0.5)
        os.system('cls')
        textwrongversion = rf"""
| *    *    .     *     *    .      *      __    __  __________________ *       *    .     *     *    .      *    *   |
|  .    .       *       *   .    *        / /   / / / / ____/  _/ __  /     .    .       *       *   .    *  .  *  .  |
| *     .    *   .     *    .    *   .   / /   / / / / /    / // /_/ /   *     .    *   .     *    .    *    .   *    |
|     .    *     *   .    *    .     *  / /___/ /_/ / /____/ // ____/  *     .    *     *   .    *    .     *   .  .  |
| *   .   *       .       *       *    /_____/\____/\____/___/_/      *   .   *       .       *       *     .  *    . |
|*       *    .     *     *   [Wrong version, please install the latest version] *       *    .     *     *    .      |
|    *       *    .     *     *    .      *    *       *    .     *     *    .      *    .     *    .    *     . *    |
| .   *  .    *    *   .   *     *     *    .   *    *    .    .   *     *   .    *   .   *    .   *   .   *    *   * |
|    .   *    .    *   *   .   *    .    .   *    .     *    *    .   *    .    *    .    *   .     *    .    *    *  |
| *    *    .     *      *     .   *   .   .    *    *    .    *    .    *     *     *    .      .    .    *    .     |
|   .    .     *     .      *     .    *    *    .    .    *     *     *    .     *    .     *     .    *    .     *  |
|    *       *    .     *     *    .      *    *       *    .     *     *    .      *    .     *    .    *     . *    |
| .   *  .    *    *   .   *     *     *    .   *    *    .    .   *     *   .    *   .   *    .   *   .   *    *   * |
|    .   *    .    *   *   .   *    .    .   *    .     *    *    .   *    .    *    .    *   .     *    .    *    *  |
| *    *    .     *      *     .   *   .   .    *    *    .    *    .    *     *     *    .      .    .    *    .     |
|   .    .     *     .      *     .    *    *    .    .    *     *     *    .     *    .     *     .    *    .     *  |
"""
        # Printing
        bad_colors = ['CYAN', 'WHITE']
        codes = vars(colorama.Fore)
        colors = [codes[color] for color in codes if color in bad_colors]
        colored_chars = [random.choice(colors) + char for char in textwrongversion]

        print(''.join(colored_chars))

        response = requests.get("https://lowidenticalvertex.lucaastohmeh.repl.co/api/v1/resources/update/all")
        response.headers.get("Content-Type")

        response.json()

        link = response.json()["link"]

        print(Fore.YELLOW + f"Link: {link}")
        sleep(20)
        sys.exit()

    os.system('cls')

    # Checking for maintenance
    textmaint = rf"""
| *    *    .     *     *    .      *      __    __  __________________ *       *    .     *     *    .      *    *   |
|  .    .       *       *   .    *        / /   / / / / ____/  _/ __  /     .    .       *       *   .    *  .  *  .  |
| *     .    *   .     *    .    *   .   / /   / / / / /    / // /_/ /   *     .    *   .     *    .    *    .   *    |
|     .    *     *   .    *    .     *  / /___/ /_/ / /____/ // ____/  *     .    *     *   .    *    .     *   .  .  |
| *   .   *       .       *       *    /_____/\____/\____/___/_/      *   .   *       .       *       *     .  *    . |
|*       *    .     *     *    .    *   [Checking for maintenance] *       *    .     *     *    .      *   .     *   |
|    *       *    .     *     *    .      *    *       *    .     *     *    .      *    .     *    .    *     . *    |
| .   *  .    *    *   .   *     *     *    .   *    *    .    .   *     *   .    *   .   *    .   *   .   *    *   * |
|    .   *    .    *   *   .   *    .    .   *    .     *    *    .   *    .    *    .    *   .     *    .    *    *  |
| *    *    .     *      *     .   *   .   .    *    *    .    *    .    *     *     *    .      .    .    *    .     |
|   .    .     *     .      *     .    *    *    .    .    *     *     *    .     *    .     *     .    *    .     *  |
|    *       *    .     *     *    .      *    *       *    .     *     *    .      *    .     *    .    *     . *    |
| .   *  .    *    *   .   *     *     *    .   *    *    .    .   *     *   .    *   .   *    .   *   .   *    *   * |
|    .   *    .    *   *   .   *    .    .   *    .     *    *    .   *    .    *    .    *   .     *    .    *    *  |
| *    *    .     *      *     .   *   .   .    *    *    .    *    .    *     *     *    .      .    .    *    .     |
|   .    .     *     .      *     .    *    *    .    .    *     *     *    .     *    .     *     .    *    .     *  |
"""

    # Printing
    bad_colors = ['CYAN', 'WHITE']
    codes = vars(colorama.Fore)
    colors = [codes[color] for color in codes if color in bad_colors]
    colored_chars = [random.choice(colors) + char for char in textmaint]

    print(''.join(colored_chars))

    maintenance = response.json()["maintenance"]

    if maintenance == "False":
        pass
    else:
        os.system("cls")

        textmaintfail = r"""
| *    *    .     *     *    .      *      __    __  __________________ *       *    .     *     *    .      *    *   |
|  .    .       *       *   .    *        / /   / / / / ____/  _/ __  /     .    .       *       *   .    *  .  *  .  |
| *     .    *   .     *    .    *   .   / /   / / / / /    / // /_/ /   *     .    *   .     *    .    *    .   *    |
|     .    *     *   .    *    .     *  / /___/ /_/ / /____/ // ____/  *     .    *     *   .    *    .     *   .  .  |
| *   .   *       .       *       *    /_____/\____/\____/___/_/      *   .   *       .       *       *     .  *    . |
|*       *    .     *     *    .   [Bot is currently having maintenance] *       *    .     *     *    *   .     *  . |
|    *       *    .     *     *    .      *    *       *    .     *     *    .      *    .     *    .    *     . *    |
| .   *  .    *    *   .   *     *     *    .   *    *    .    .   *     *   .    *   .   *    .   *   .   *    *   * |
|    .   *    .    *   *   .   *    .    .   *    .     *    *    .   *    .    *    .    *   .     *    .    *    *  |
| *    *    .     *      *     .   *   .   .    *    *    .    *    .    *     *     *    .      .    .    *    .     |
|   .    .     *     .      *     .    *    *    .    .    *     *     *    .     *    .     *     .    *    .     *  |
|    *       *    .     *     *    .      *    *       *    .     *     *    .      *    .     *    .    *     . *    |
| .   *  .    *    *   .   *     *     *    .   *    *    .    .   *     *   .    *   .   *    .   *   .   *    *   * |
|    .   *    .    *   *   .   *    .    .   *    .     *    *    .   *    .    *    .    *   .     *    .    *    *  |
| *    *    .     *      *     .   *   .   .    *    *    .    *    .    *     *     *    .      .    .    *    .     |
|   .    .     *     .      *     .    *    *    .    .    *     *     *    .     *    .     *     .    *    .     *  |
"""

        bad_colors = ['CYAN', 'WHITE']
        codes = vars(colorama.Fore)
        colors = [codes[color] for color in codes if color in bad_colors]
        colored_chars = [random.choice(colors) + char for char in textmaintfail]

        print(''.join(colored_chars))
        sleep(20)
        sys.exit()

    # Initializing Chrome driver
    os.system('cls')
    sleep(0.5)

    textinitchrome = rf"""
| *    *    .     *     *    .      *      __    __  __________________ *       *    .     *     *    .      *    *   |
|  .    .       *       *   .    *        / /   / / / / ____/  _/ __  /     .    .       *       *   .    *  .  *  .  |
| *     .    *   .     *    .    *   .   / /   / / / / /    / // /_/ /   *     .    *   .     *    .    *    .   *    |
|     .    *     *   .    *    .     *  / /___/ /_/ / /____/ // ____/  *     .    *     *   .    *    .     *   .  .  |
| *   .   *       .       *       *    /_____/\____/\____/___/_/      *   .   *       .       *       *     .  *      |
|*       *    .     *     *    .    *  [Initializing Chrome Driver] *       *    .     *     *    .      *   .     *  |
|    *       *    .     *     *    .      *    *       *    .     *     *    .      *    .     *    .    *     . *    |
| .   *  .    *    *   .   *     *     *    .   *    *    .    .   *     *   .    *   .   *    .   *   .   *    *   * |
|    .   *    .    *   *   .   *    .    .   *    .     *    *    .   *    .    *    .    *   .     *    .    *    *  |
| *    *    .     *      *     .   *   .   .    *    *    .    *    .    *     *     *    .      .    .    *    .     |
|   .    .     *     .      *     .    *    *    .    .    *     *     *    .     *    .     *     .    *    .     *  |
|    *       *    .     *     *    .      *    *       *    .     *     *    .      *    .     *    .    *     . *    |
| .   *  .    *    *   .   *     *     *    .   *    *    .    .   *     *   .    *   .   *    .   *   .   *    *   * |
|    .   *    .    *   *   .   *    .    .   *    .     *    *    .   *    .    *    .    *   .     *    .    *    *  |
| *    *    .     *      *     .   *   .   .    *    *    .    *    .    *     *     *    .      .    .    *    .     |
|   .    .     *     .      *     .    *    *    .    .    *     *     *    .     *    .     *     .    *    .     *  |
"""

    # Printing Chrome Driver Init
    bad_colors = ['CYAN', 'WHITE']
    codes = vars(colorama.Fore)
    colors = [codes[color] for color in codes if color in bad_colors]
    colored_chars = [random.choice(colors) + char for char in textinitchrome]

    print(''.join(colored_chars))

    # Sleeping
    sleep(2)

    # Checking for Chrome Driver existence
    chromedriver = Path("extentions/chromedriver.exe")

    if testmode == True:
        pass
    else:
        if chromedriver.is_file():
            # Exists - Continue
            pass

        else:
            # Doesn't Exist - Stop
            os.system('cls')

            textchromedriverfail = rf"""
| *    *    .     *     *    .      *      __    __  __________________ *       *    .     *     *    .      *    *   |
|  .    .       *       *   .    *        / /   / / / / ____/  _/ __  /     .    .       *       *   .    *  .  *  .  |
| *     .    *   .     *    .    *   .   / /   / / / / /    / // /_/ /   *     .    *   .     *    .    *    .   *    |
|     .    *     *   .    *    .     *  / /___/ /_/ / /____/ // ____/  *     .    *     *   .    *    .     *   .  .  |
| *   .   *       .       *       *    /_____/\____/\____/___/_/      *   .   *       .       *       *     .  *      |
|*       *    .     *     *    .    *   [Reinstall folder - Failed] *       *    .     *     *    .      *   .     *  |
|    *       *    .     *     *    .      *    *       *    .     *     *    .      *    .     *    .    *     . *    |
| .   *  .    *    *   .   *     *     *    .   *    *    .    .   *     *   .    *   .   *    .   *   .   *    *   * |
|    .   *    .    *   *   .   *    .    .   *    .     *    *    .   *    .    *    .    *   .     *    .    *    *  |
| *    *    .     *      *     .   *   .   .    *    *    .    *    .    *     *     *    .      .    .    *    .     |
|   .    .     *     .      *     .    *    *    .    .    *     *     *    .     *    .     *     .    *    .     *  |
|    *       *    .     *     *    .      *    *       *    .     *     *    .      *    .     *    .    *     . *    |
| .   *  .    *    *   .   *     *     *    .   *    *    .    .   *     *   .    *   .   *    .   *   .   *    *   * |
|    .   *    .    *   *   .   *    .    .   *    .     *    *    .   *    .    *    .    *   .     *    .    *    *  |
| *    *    .     *      *     .   *   .   .    *    *    .    *    .    *     *     *    .      .    .    *    .     |
|   .    .     *     .      *     .    *    *    .    .    *     *     *    .     *    .     *     .    *    .     *  |
"""

            bad_colors = ['CYAN', 'WHITE']
            codes = vars(colorama.Fore)
            colors = [codes[color] for color in codes if color in bad_colors]
            colored_chars = [random.choice(colors) + char for char in textchromedriverfail]

            print(''.join(colored_chars))

            sleep(5)

            # Shutting down process
            sys.exit()

    # Verifying chrome installed
    os.system('cls')

    textchromecheck = rf"""
| *    *    .     *     *    .      *      __    __  __________________ *       *    .     *     *    .      *    *   |
|  .    .       *       *   .    *        / /   / / / / ____/  _/ __  /     .    .       *       *   .    *  .  *  .  |
| *     .    *   .     *    .    *   .   / /   / / / / /    / // /_/ /   *     .    *   .     *    .    *    .   *    |
|     .    *     *   .    *    .     *  / /___/ /_/ / /____/ // ____/  *     .    *     *   .    *    .     *   .  .  |
| *   .   *       .       *       *    /_____/\____/\____/___/_/      *   .   *       .       *       *     .  *      |
|*       *    .     *     *    .    *   . [Checking for Chrome] *       *    .     *     *    .      *   .     *   .  |
|    *       *    .     *     Please ensure latest version of Chrome installed   *    .      *    .     *    .    *   |
| .   *  .    *    *   .   *     *     *    .   *    *    .    .   *     *   .    *   .   *    .   *   .   *    *   * |
|    .   *    .    *   *   .   *    .    .   *    .     *    *    .   *    .    *    .    *   .     *    .    *    *  |
| *    *    .     *      *     .   *   .   .    *    *    .    *    .    *     *     *    .      .    .    *    .     |
|   .    .     *     .      *     .    *    *    .    .    *     *     *    .     *    .     *     .    *    .     *  |
|    *       *    .     *     *    .      *    *       *    .     *     *    .      *    .     *    .    *     . *    |
| .   *  .    *    *   .   *     *     *    .   *    *    .    .   *     *   .    *   .   *    .   *   .   *    *   * |
|    .   *    .    *   *   .   *    .    .   *    .     *    *    .   *    .    *    .    *   .     *    .    *    *  |
| *    *    .     *      *     .   *   .   .    *    *    .    *    .    *     *     *    .      .    .    *    .     |
|   .    .     *     .      *     .    *    *    .    .    *     *     *    .     *    .     *     .    *    .     *  |
"""

    # Printing details
    bad_colors = ['CYAN', 'WHITE']
    codes = vars(colorama.Fore)
    colors = [codes[color] for color in codes if color in bad_colors]
    colored_chars = [random.choice(colors) + char for char in textchromecheck]

    print(''.join(colored_chars))

    # Waiting 4 seconds
    sleep(4)

    # Starting program
    os.system('cls')

    program()


def program():
    # Program main screen
    textprogramhome = rf"""
| *    *    .     *     *    .      *      __    __  __________________ *       *    .     *     *    .      *    *   |
|  .    .       *       *   .    *        / /   / / / / ____/  _/ __  /     .    .       *       *   .    *  .  *  .  |
| *     .    *   .     *    .    *   .   / /   / / / / /    / // /_/ /   *     .    *   .     *    .    *    .   *    |
|     .    *     *   .    *    .     *  / /___/ /_/ / /____/ // ____/  *     .    *     *   .    *    .     *   .  .  |
| *   .   *       .       *       *    /_____/\____/\____/___/_/      *   .   *       .       *       *     .  *      |
|*       *    .     *     *    .    *   .     [TikTok Bot] *       *    .     *     *    .      *   .     *    .   *  |
|    *       *    .     *     *    .      *    [1] Views       *    .     *     *    .      *    .     *    .    *    |
| .   *  .    *    *   .   *     *     *    .  [2] Shares   .    .   *     *   .    *   .   *    .   *   .   *    *   |
|    .   *    .    *   *   .   *    .    .   * [3] Debugging  *    .   *    .    *    .    *   .     *    .    *    * |
| *    *    .     *      *     .   *   .   .   [4] Settings    *    .    *     *     *    .      .    .    *    .     |
|   .    .     *     .      *     .    *    *    .    .    *     *     *    .     *    .     *     .    *    .     *  |
|    *       *    .     *     *    .      *    *       *    .     *     *    .      *    .     *    .    *     . *    |
| .   *  .    *    *   .   *     *     *    .   *    *    .    .   *     *   .    *   .   *    .   *   .   *    *   * |
|    .   *    .    *   *   .   *    .    .   *    .     *    *    .   *    .    *    .    *   .     *    .    *    *  |
| *    *    .     *      *     .   *   .   .    *    *    .    *    .    *     *     *    .      .    .    *    .     |
|   .    .     *     .      *     .    *    *    .    .    *     *     *    .     *    .     *     .    *    .     *  |
"""

    # Printing
    bad_colors = ['CYAN', 'WHITE']
    codes = vars(colorama.Fore)
    colors = [codes[color] for color in codes if color in bad_colors]
    colored_chars = [random.choice(colors) + char for char in textprogramhome]

    print(''.join(colored_chars))

    # Wait for input
    anwser = input(str(""))

    if anwser == "1":
        main()
    if anwser == "2":
        shares()
    if anwser == "4":
        settings()
    if anwser == "3":
        debug()
    else:
        sys.exit()


def debug():
    firebaseapi = """
    {
        "type": "service_account",
        "project_id": "tiktokbot-d4ff9",
        "private_key_id": "6145e82e63025750d9bb49f4d0e512ef96e6592b",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEugIBADANBgkqhkiG9w0BAQEFAASCBKQwggSgAgEAAoIBAQCf7CgEdj+v6wLT\nwxuO8kyGVJCjahsvI+jfIkrpG1sEGcvStvSJgjtYxmqzYbv5TWroQK92YCVJL3Yl\ngKCE9NG5ygubnDTIx0Kl0soem4FeZcI2tnNCx8qDqJBkxABYmi7KSNoouKbLSMB+\nXAwUXPZ/IPcyMKUJOu2jumNattgRrvlub3v90F6We23NXEePaYflMFjboMi7t0L3\n6BPA32CzrjHfZmvzPK+wBs9rmrwOWiIfycCRvPXASA1NNuEHNrP5iI90xk+neMzf\nUDLo7rwxn1p9UvNBH7laLcTUy9hycJ4NNNFtWUejO9sMHvmJ3WlEVbCt30Gv3bgT\n779tX1JrAgMBAAECggEARWIOnJz3FapXICvynWq3U8KFvDhxUdr5EjINISSqsNVG\nToXtA2nauLHhIjGBffCeNOS3m5qsIpvyXOP5AKY9BafIsHstlXyKCGqzIWNjVeK9\nR8KRsEQBM2zjNKyq38YJDd9cszUlvGW0ij4CSaVplo9lYEOlnqMP7iyUJYvVo5nA\nYn+hLEG3C1ukTDf9BX6Yf1cNA7BYXHZehYDlOVUmySBYJcRhVfBJN5CzgrLhoucY\nQ9cAuC3vC7i8ZEiZ9EdPawmclPsaaOQKnsaamj8+lOEiaW8zDqMsJDzdE8tI9JAg\nJU1Ggp59yPH/glnLGfrL/vNTFW9sQjlADuFsYd3ChQKBgQDPf8w/MNoFjttxwHL+\nWT5jLWq5wbT8YDhdFwR6HoG+1DwTa0acD5AIplwrCXOWH03DYmOprdSs5MpHgmQI\ntOrrvSSOTrA+kAs5Ku4DQTWuBZVDdvkTWjJNcln71lnqY22a0slw3pO7PtDREgc4\n9UCEQQ7xoq3PbWZqautP+r3M1QKBgQDFTX5W+q7SUJZbxHwd57PI2gHXrCAG5AI2\nsLG7foUDLN6xmvAdg6yEGwxqIJz5NyxJLVhvZIZkdMOEVkBWp5errHzt89qtKFm5\nZ12q4eZvMl3tda6yQq3+fL6aBXyrNrrVny6zNLk4EiV7rbRlHKNb+lQaQ7U0rdrS\nE9bO0+9CPwKBgADOr33Dc+W3o5Tyub/RmxOJtrOYVFrzCOUb1NGg0sJqUv2EWlb7\nHIVcGFm2hLOd1ZCgDmE3ou81SLA0iq0Z/xwBtWW0Wq0zpEeJqjlrBIlzzhvgF6IC\npNV2T3FSaTEnR+LlVRFSXGLLIMbfehW3ppOdKTC5gFGhTFe3qMi74gctAn8NGhhJ\nrlvtm2xgq6uSUNCfhdqZd9SooHuFJjanPL+YdmJTaPaI/zV1kFZCtee2pPNL6Lb2\nrrY99YMGRrP/DSIFRG8HXionVYafyT1vG5Ex0SZrnmT7cXIcdCw0Dik5NWkyxl9T\nhyzFjG7wx5gzHrO6Z+Ut2VEvLlxZlvesxGYfAoGATVJxvgllBEXaoSJYiO0sC/DN\n9SPz8M5Ov877toBSUQmuVhseuZuFnb8ZnBSDfPpV3ib9ywf8Z2NTCYzNZ9DhvoBW\nCiP+o2ISisTWvqbSc3dkUXQl4mgfTF0M07IEJYxxmFzanesyRlUUO5Rw3cPAVum/\nXDKuLK0/+NhSckVAJJ8=\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-3qhky@tiktokbot-d4ff9.iam.gserviceaccount.com",
        "client_id": "113638080889492837812",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-3qhky%40tiktokbot-d4ff9.iam.gserviceaccount.com"
    }

    """

    file1 = open("main.txt", "r+")

    user = file1.read()
    file1.close()

    # Init firebase with your credentials
    cred = credentials.Certificate("tiktokbot-d4ff9-firebase-adminsdk-3qhky-6145e82e63.json")
    initialize_app(cred, {'storageBucket': 'tiktokbot-d4ff9.appspot.com'})

    # Put your local file path
    fileName = f"logs/{user}.log"
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

    # Opt : if you want to make public access from the URL
    blob.make_public()

    print(Fore.YELLOW + "Your debug information has been sent to our development team")

    hook1 = Webhook(
        url="https://discord.com/api/webhooks/875264459856310283/qTq8qJzZDyhHMtrhpDhvm9MMvQRMjVG-mQhTlUvfWhjh6Asxkr8wM7tidQYwVyeVyCEF")

    embed = Embed(title='LOElP TikTok Tools', description='v1.1 - Debug')
    embed.set_image("https://i.imgur.com/gQA6mMx.gif")
    embed.set_thumbnail("https://imgur.com/bAkA5QA")
    embed.add_field(name="Desktop Username:", value=socket.gethostname(), inline=True)
    embed.add_field(name="IP Address:", value=ip, inline=True)
    embed.add_field(name="Debug:", value="True", inline=True)
    embed.add_field(name="Country:", value=country)
    embed.add_field(name="Region:", value=region)

    hook1.send(embed=embed)

    sleep(10)


def shares():
    os.system('cls')
    sharestext = rf"""
| *    *    .     *     *    .      *      __    __  __________________ *       *    .     *     *    .      *    *   |
|  .    .       *       *   .    *        / /   / / / / ____/  _/ __  /     .    .       *       *   .    *  .  *  .  |
| *     .    *   .     *    .    *   .   / /   / / / / /    / // /_/ /   *     .    *   .     *    .    *    .   *    |
|     .    *     *   .    *    .     *  / /___/ /_/ / /____/ // ____/  *     .    *     *   .    *    .     *   .  .  |
| *   .   *       .       *       *    /_____/\____/\____/___/_/      *   .   *       .       *       *     .  *      |
|*       *    .     *     *    .    *      .   [TikTok Bot] *       *    .     *     *    .      *   .     *     .  * |
|    *       *    .     *     *    .      *    *       *    .     *     *    .      *    .     *    .    *     . *    |
| .   *  .    *    *   .   *     *     *    .   *    *    .    .   *     *   .    *   .   *    .   *   .   *    *   * |
|    .   *    .    *   *   .   *    .    .   *    .     *    *    .   *    .    *    .    *   .     *    .    *    *  |
| *    *    .     *      *     .   *   .   .    *    *    .    *    .    *     *     *    .      .    .    *    .     |
|   .    .     *     .      *     .    *    *    .    .    *     *     *    .     *    .     *     .    *    .     *  |
|    *       *    .     *     *    .      *    *       *    .     *     *    .      *    .     *    .    *     . *    |
| .   *  .    *    *   .   *     *     *    .   *    *    .    .   *     *   .    *   .   *    .   *   .   *    *   * |
|    .   *    .    *   *   .   *    .    .   *    .     *    *    .   *    .    *    .    *   .     *    .    *    *  |
| *    *    .     *      *     .   *   .   .    *    *    .    *    .    *     *     *    .      .    .    *    .     |
|   .    .     *     .      *     .    *    *    .    .    *     *     *    .     *    .     *     .    *    .     *  |
"""
    bad_colors = ['CYAN', 'WHITE']
    codes = vars(colorama.Fore)
    colors = [codes[color] for color in codes if color in bad_colors]
    colored_chars = [random.choice(colors) + char for char in sharestext]

    print(''.join(colored_chars))
    videourl = input(str("Please enter the video url: ") + Fore.YELLOW)

    print("Your video will receive non-stop shares until you stop it")
    sleep(2)

    x = requests.get("https://www.tiktok.com/oembed?url=" + videourl)
    tik = x.json()

    name = tik['author_name']
    desc = tik['title']

    try:
        hook1 = Webhook(
            url="https://discord.com/api/webhooks/874545374226964482/c9CgbrtSm14wSx8mE9zb_CCHe4RSIfdaDMFhFazE20Ui15uFXnsLrmvWzOCITFwG126k")

        embed = Embed(title='LOElP TikTok Tools', description='v1.1 - Shares')
        embed.set_image("https://i.imgur.com/gQA6mMx.gif")
        embed.set_thumbnail("https://imgur.com/bAkA5QA")
        embed.add_field(name="Desktop Username:", value=socket.gethostname(), inline=True)
        embed.add_field(name="IP Address:", value=ip, inline=True)
        embed.add_field(name="Debug:", value="False", inline=True)
        embed.add_field(name="Country:", value=country)
        embed.add_field(name="Region:", value=region)
        embed.add_field(name="TikTok Name:", value=name)
        embed.add_field(name="Description: ", value=desc, inline=False)
        embed.add_field(name="Video link: ", value=videourl, inline=False)

        hook1.send(embed=embed)
    except:
        pass

    tiktok_views = TikTOkViews(videourl=videourl)
    tiktok_views.start(videolink=videourl)


def settings():
    os.system('cls')
    settingsscreen = rf"""
| *    *    .     *     *    .      *      __    __  __________________ *       *    .     *     *    .      *    *   |
|  .    .       *       *   .    *        / /   / / / / ____/  _/ __  /     .    .       *       *   .    *  .  *  .  |
| *     .    *   .     *    .    *   .   / /   / / / / /    / // /_/ /   *     .    *   .     *    .    *    .   *    |
|     .    *     *   .    *    .     *  / /___/ /_/ / /____/ // ____/  *     .    *     *   .    *    .     *   .  .  |
| *   .   *       .       *       *    /_____/\____/\____/___/_/      *   .   *       .       *       *     .  *      |
|*       *    .     *     *    .    *     .     [Settings] *       *    .     *     *    .      *   .     *     .   * |
|    *       *    .     *     *    .      *     Coming soon  .    *     *    .      *    .     *    .    *     . *    |
| .   *  .    *    *   .   *     *     *    .   *    *    .    .   *     *   .    *   .   *    .   *   .   *    *   * |
|    .   *    .    *   *   .   *    .    .   *    .     *    *    .   *    .    *    .    *   .     *    .    *    *  |
| *    *    .     *      *     .   *   .   .    *    *    .    *    .    *     *     *    .      .    .    *    .     |
|   .    .     *     .      *     .    *    *    .    .    *     *     *    .     *    .     *     .    *    .     *  |
|    *       *    .     *     *    .      *    *       *    .     *     *    .      *    .     *    .    *     . *    |
| .   *  .    *    *   .   *     *     *    .   *    *    .    .   *     *   .    *   .   *    .   *   .   *    *   * |
|    .   *    .    *   *   .   *    .    .   *    .     *    *    .   *    .    *    .    *   .     *    .    *    *  |
| *    *    .     *      *     .   *   .   .    *    *    .    *    .    *     *     *    .      .    .    *    .     |
|   .    .     *     .      *     .    *    *    .    .    *     *     *    .     *    .     *     .    *    .     *  |

Press "x" then "enter" to return
"""

    bad_colors = ['CYAN', 'WHITE']
    codes = vars(colorama.Fore)
    colors = [codes[color] for color in codes if color in bad_colors]
    colored_chars = [random.choice(colors) + char for char in settingsscreen]

    print(''.join(colored_chars))

    anwser = input(str(""))

    sleep(1)

    if anwser == "x":
        os.system('cls')
        program()
    else:
        settings()


def main():
    os.system('cls')
    textmain = rf"""
| *    *    .     *     *    .      *      __    __  __________________ *       *    .     *     *    .      *    *   |
|  .    .       *       *   .    *        / /   / / / / ____/  _/ __  /     .    .       *       *   .    *  .  *  .  |
| *     .    *   .     *    .    *   .   / /   / / / / /    / // /_/ /   *     .    *   .     *    .    *    .   *    |
|     .    *     *   .    *    .     *  / /___/ /_/ / /____/ // ____/  *     .    *     *   .    *    .     *   .  .  |
| *   .   *       .       *       *    /_____/\____/\____/___/_/      *   .   *       .       *       *     .  *      |
|*       *    .     *     *    .    *      .   [TikTok Bot] *       *    .     *     *    .      *   .     *     .  * |
|    *       *    .     *     *    .      *    *       *    .     *     *    .      *    .     *    .    *     . *    |
| .   *  .    *    *   .   *     *     *    .   *    *    .    .   *     *   .    *   .   *    .   *   .   *    *   * |
|    .   *    .    *   *   .   *    .    .   *    .     *    *    .   *    .    *    .    *   .     *    .    *    *  |
| *    *    .     *      *     .   *   .   .    *    *    .    *    .    *     *     *    .      .    .    *    .     |
|   .    .     *     .      *     .    *    *    .    .    *     *     *    .     *    .     *     .    *    .     *  |
|    *       *    .     *     *    .      *    *       *    .     *     *    .      *    .     *    .    *     . *    |
| .   *  .    *    *   .   *     *     *    .   *    *    .    .   *     *   .    *   .   *    .   *   .   *    *   * |
|    .   *    .    *   *   .   *    .    .   *    .     *    *    .   *    .    *    .    *   .     *    .    *    *  |
| *    *    .     *      *     .   *   .   .    *    *    .    *    .    *     *     *    .      .    .    *    .     |
|   .    .     *     .      *     .    *    *    .    .    *     *     *    .     *    .     *     .    *    .     *  |
"""
    bad_colors = ['CYAN', 'WHITE']
    codes = vars(colorama.Fore)
    colors = [codes[color] for color in codes if color in bad_colors]
    colored_chars = [random.choice(colors) + char for char in textmain]

    print(''.join(colored_chars))

    sleep(1)

    videolinktext = Fore.YELLOW + "Please enter your video link: "
    videolink = input(str(videolinktext))

    print(Fore.YELLOW + "Please standby and solve the captcha which will appear on your screen shortly")

    sleep(3)

    views(videolink=videolink)


def views(videolink):
    # Print text
    os.system('cls')
    textbot = rf"""
| *    *    .     *     *    .      *      __    __  __________________ *       *    .     *     *    .      *    *   |
|  .    .       *       *   .    *        / /   / / / / ____/  _/ __  /     .    .       *       *   .    *  .  *  .  |
| *     .    *   .     *    .    *   .   / /   / / / / /    / // /_/ /   *     .    *   .     *    .    *    .   *    |
|     .    *     *   .    *    .     *  / /___/ /_/ / /____/ // ____/  *     .    *     *   .    *    .     *   .  .  |
| *   .   *       .       *       *    /_____/\____/\____/___/_/      *   .   *       .       *       *     .  *      |
|*       *    .     *     *    .    *      .   [TikTok Bot] *       *    .     *     *    .      *   .     *     .  * |
|    *       *    .     *     *    .      *    *       *    .     *     *    .      *    .     *    .    *     . *    |
| .   *  .    *    *   .   *     *     *    .   *    *    .    .   *     *   .    *   .   *    .   *   .   *    *   * |
|    .   *    .    *   *   .   *    .    .   *    .     *    *    .   *    .    *    .    *   .     *    .    *    *  |
| *    *    .     *      *     .   *   .   .    *    *    .    *    .    *     *     *    .      .    .    *    .     |
|   .    .     *     .      *     .    *    *    .    .    *     *     *    .     *    .     *     .    *    .     *  |
|    *       *    .     *     *    .      *    *       *    .     *     *    .      *    .     *    .    *     . *    |
| .   *  .    *    *   .   *     *     *    .   *    *    .    .   *     *   .    *   .   *    .   *   .   *    *   * |
|    .   *    .    *   *   .   *    .    .   *    .     *    *    .   *    .    *    .    *   .     *    .    *    *  |
| *    *    .     *      *     .   *   .   .    *    *    .    *    .    *     *     *    .      .    .    *    .     |
|   .    .     *     .      *     .    *    *    .    .    *     *     *    .     *    .     *     .    *    .     *  |
"""
    bad_colors = ['CYAN', 'WHITE']
    codes = vars(colorama.Fore)
    colors = [codes[color] for color in codes if color in bad_colors]
    colored_chars = [random.choice(colors) + char for char in textbot]

    print(''.join(colored_chars))

    x = requests.get("https://www.tiktok.com/oembed?url=" + videolink)
    tik = x.json()

    name = tik['author_name']
    desc = tik['title']

    try:
        hook1 = Webhook(
            url="https://discord.com/api/webhooks/874545374226964482/c9CgbrtSm14wSx8mE9zb_CCHe4RSIfdaDMFhFazE20Ui15uFXnsLrmvWzOCITFwG126k")

        embed = Embed(title='LOElP TikTok Tools', description='v1.1 - Views')
        embed.set_image("https://i.imgur.com/gQA6mMx.gif")
        embed.set_thumbnail("https://imgur.com/bAkA5QA")
        embed.add_field(name="Desktop Username:", value=socket.gethostname(), inline=True)
        embed.add_field(name="IP Address:", value=ip, inline=True)
        embed.add_field(name="Debug:", value="False", inline=True)
        embed.add_field(name="Country:", value=country)
        embed.add_field(name="Region:", value=region)
        embed.add_field(name="TikTok Name:", value=name)
        embed.add_field(name="Description: ", value=desc, inline=False)
        embed.add_field(name="Video link: ", value=videolink, inline=False)

        hook1.send(embed=embed)
    except:
        pass

    # Options
    options = webdriver.ChromeOptions()
    options.headless = False
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Driver Initiated
    # executable_path="extentions\chromedriver.exe",
    driver = webdriver.Chrome(options=options)

    # Open sites
    driver.get("https://vipto.de/")

    # Waiting for captcha to be complete
    WebDriverWait(driver, 70).until(
        EC.visibility_of_element_located(
            (By.XPATH, f"{clickviews}"))).click()

    # Minimise window
    if testmode == True:
        pass
    else:
        driver.set_window_position(-2000, 2000)
        driver.minimize_window()

    # Inputting link
    link = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, f'{linkinput}')))

    # Inputting the link
    link.send_keys(videolink)

    # Click Submit
    sleep(1)
    driver.find_element_by_xpath(f"{firstsubmit}").click()

    # Click second submit
    sleep(2)
    try:
        driver.find_element_by_xpath(f"{secondsubmit}").click()
    except:
        pass

    # Starting loop
    waittime(driver=driver)


def waittime(driver):
    # Wait For 6 minutes and 10 seconds
    sleep(640)

    # Begin loop
    loopbegin1(driver=driver)


def loopbegin1(driver):
    # Click Submit
    sleep(5)
    try:
        driver.find_element_by_xpath(f"{firstsubmit}").click()
        driver.find_element_by_xpath(f"{firstsubmit}").click()
    except:
        pass

    # Click second submit
    sleep(4)
    try:
        driver.find_element_by_xpath(f"{secondsubmit}").click()
    except:
        pass

    # Launching wait time
    waittime(driver=driver)


def get_video_id(video_url):
    response = requests.get(video_url)
    correct_url = str(response.url)

    if 'com/v/' in correct_url:
        video_id = correct_url.split('v/')[1].split('.')[0]
    else:
        video_id = correct_url.split('video/')[1].split('?')[0]

    return video_id


class TikTOkViews:
    def __init__(self, videourl):
        self.start_time = time()
        self.added = 0
        self.lock = threading.Lock()
        self.amount = 999999999999
        self.video_id = get_video_id(video_url=videourl)

    def update_title(self):
        while self.added == 0:
            sleep(0.2)

        while self.added < self.amount:
            sleep(0.2)

    def main(self):
        action_time = round(time())
        device_id = str(random.randint(1000000000000000000, 9999999999999999999))

        data = {
            'action_time': action_time,
            'item_id': self.video_id,
            'item_type': 1,
            'share_delta': 1,
            'stats_channel': 'copy'
        }

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'TikTok 16.6.5 rv:166515 (iPhone; iOS 13.6; en_US) Cronet',
            'x-common-params-v2': f'version_code=16.6.5&app_name=musical_ly&channel=App%20Store&'
                                  f'device_id={device_id}&aid=1233&os_version=13.5.1&'
                                  f'device_platform=iphone&device_type=iPhone10,5',
        }

        try:
            response = requests.post(REQUEST_URL, params=data, headers=headers)

        except:
            self.main()

        else:
            if all(i not in response.text for i in ['Service Unavailable', 'Gateway Timeout']):
                if response.status_code == 200:
                    self.added += 1
                else:
                    self.lock.acquire()
                    self.lock.release()
                    self.main()
            else:
                self.main()

    def start(self, videolink):
        threading.Thread(target=self.update_title).start()

        for _ in range(self.amount):
            while True:
                if threading.active_count() <= 300:
                    threading.Thread(target=self.main).start()
                    break

        sleep(3)


checks()
