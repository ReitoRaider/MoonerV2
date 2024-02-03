from colorama import init, Fore; init()
import platform
import sys
import os
from datetime import datetime
import re

# needed for printing shit btw
if platform.system() == 'Windows':
    os.system(f"mode con: cols=170 lines=35")
elif platform.system() == 'Linux':
    os.system(f"resize -s 170 35")

class c:
    r = Fore.RED
    lr = Fore.LIGHTRED_EX
    y = Fore.YELLOW
    ly = Fore.LIGHTYELLOW_EX
    g = Fore.GREEN
    lg = Fore.LIGHTGREEN_EX
    res = Fore.RESET
    p = Fore.LIGHTMAGENTA_EX
    m = Fore.MAGENTA
    o = "\033[38;2;255;165;0m"
    do = "\033[38;2;200;120;0m"
    b = Fore.LIGHTBLACK_EX

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    elif platform.system() == 'Linux':
        os.system('clear')

def title(tit):
    if platform.system() == 'Windows':
        os.system(f'title {tit}')
    elif platform.system() == 'Linux':
        sys.stdout.write(f"\x1b]0;{tit}\x07")

# printing shit
size = os.get_terminal_size().columns
def visible_length(string):
    escape_code_pattern = r'\033\[[0-9;]*[mG]'
    return len(re.sub(escape_code_pattern, '', string))

def center_line(line, total_length):
    padding_length = (total_length - visible_length(line)) // 2
    padding = ' ' * padding_length
    return padding + line

def bprint(banner):
    lines = banner.split('\n')
    for line in lines:
        centered_line = center_line(line, size)
        print(centered_line)

class log:
    def get():
        current_datetime = datetime.now()
        return current_datetime.strftime('%H:%M:%S')
    def ask(pyt):
        return input(f"{c.r}║{c.res}{pyt}{c.r}║ {c.res}> ")
    def askyn(pyt):
        return input(f"{c.r}║{c.res}{pyt}{c.r}║ {c.b}(y/n) {c.res}> ")
    
    def g(status, text, token):
        if text != "":
            text = f"({text})"
        if len(text) > 100:
            text = ""
        print(f"{c.b}[{log.get()}]{c.res} | {c.g}[{status}]{c.res} | {token[:30]}{c.r}***{c.b} {text} [GOOD]")

    def c(status, text, token):
        if text != "":
            text = f"({text})"
        if len(text) > 100:
            text = ""
        print(f"{c.b}[{log.get()}]{c.res} | {c.y}[{status}]{c.res} | {token[:30]}{c.r}***{c.b} {text} [CAPTCHA]")

    def r(status, text, token):
        if text != "":
            text = f"({text})"
        if len(text) > 100:
            text = ""
        print(f"{c.b}[{log.get()}]{c.res} | {c.y}[{status}]{c.res} | {token[:30]}{c.r}***{c.b} {text} [RATELIMIT]")

    def i(status, text, token):
        if text != "":
            text = f"({text})"
        if len(text) > 100:
            text = ""
        print(f"{c.b}[{log.get()}]{c.res} | {c.r}[{status}]{c.res} | {token[:30]}{c.r}***{c.b} {text} [INVALID]")

    def un(status, text, token):
        if text != "":
            text = f"({text})"
        if len(text) > 100:
            text = ""
        print(f"{c.b}[{log.get()}]{c.res} | {c.b}[{status}]{c.res} | {token[:30]}{c.r}***{c.b} {text} [UNKNOWN ERROR]")

    class checker:
        def g(token):
            print(f"{c.b}[{log.get()}]{c.res} | {c.g}[UNLOCKED]{c.res} | {token[:30]}{c.r}***{c.b}")

        def l(token):
            print(f"{c.b}[{log.get()}]{c.res} | {c.y}[LOCKED]{c.res}   | {token[:30]}{c.r}***{c.b}")

        def r(token):
            print(f"{c.b}[{log.get()}]{c.res} | {c.y}[RATELIMIT]{c.res} | {token[:30]}{c.r}***{c.b}")

        def i(token):
            print(f"{c.b}[{log.get()}]{c.res} | {c.r}[INVALID]{c.res}  | {token[:30]}{c.r}***{c.b}")