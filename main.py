import random
import string
import colorama

from colorama import Fore, Style, init


def ascii():
    print(f"""{Fore.RED} {Style.BRIGHT}
 ███▄    █ ▓█████  █    ██ ▄▄▄█████▓ ██▀███   ▒█████   ███▄    █ 
 ██ ▀█   █ ▓█   ▀  ██  ▓██▒▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒ ██ ▀█   █ 
▓██  ▀█ ██▒▒███   ▓██  ▒██░▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒▓██  ▀█ ██▒
▓██▒  ▐▌██▒▒▓█  ▄ ▓▓█  ░██░░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░▓██▒  ▐▌██▒
▒██░   ▓██░░▒████▒▒▒█████▓   ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░▒██░   ▓██░
░ ▒░   ▒ ▒ ░░ ▒░ ░░▒▓▒ ▒ ▒   ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
░ ░░   ░ ▒░ ░ ░  ░░░▒░ ░ ░     ░      ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░░   ░ ▒░
   ░   ░ ░    ░    ░░░ ░ ░   ░        ░░   ░ ░ ░ ░ ▒     ░   ░ ░ 
         ░    ░  ░   ░                 ░         ░ ░           ░ 
     
                                                                 
                   ({Fore.YELLOW}MODULE{Fore.RED}) » {Fore.YELLOW} Email Gen{Fore.RESET}                                          
""")


def emailgenphanton():
    outpath = input(
        " Enter The File Path you would like to save it to\n (make sure the text file is empty):  ")
    f = open(outpath, "w")

    def random_char(char_num):
        return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

    for i in range(1000):
        f.write(random_char(7)+"@gmail.com:"+random_char(7)+("\n"))
    f.close()
    input("press Enter to Exit")


emailgenphanton()
