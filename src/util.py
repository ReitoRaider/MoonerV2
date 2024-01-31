from colorama import init, Fore; init()
import platform
import sys
import os

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

class log:
    def ask(pyt):
        return input(f"{c.r}║{c.res}{pyt}{c.r}║ {c.res}> ")
    def askyn(pyt):
        return input(f"{c.r}║{c.res}{pyt}{c.r}║ {c.b}(y/n) {c.res}> ")