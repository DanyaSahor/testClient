import configparser
import socket
import threading
from pyfiglet import Figlet
from colorama import *
from time import *
import requests   

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class messages:
    prefix = "[Katana]"
    nonet = "Отсутствует интернет соединение."
    prsent = "Нажмите:"
    enter = "Enter"
    fexit = "Чтобы выйти."
    space = " "
prefix = "Katana "
print(color.BOLD + '')
init()

config = configparser.ConfigParser()
config.read("config.ini")
print(Fore.MAGENTA + '')
f = Figlet(font='slant')
print (f.renderText('       Katana'))
print('-------------------------------------------------------------------')
print(Fore.WHITE + "")

def checkinternet():
    try:
        timeout = 20
        requests.head("http://www.google.com/",  timeout=timeout)
    except requests.ConnectionError:
        print(messages.prefix + messages.space + color.RED + messages.nonet + Fore.WHITE)
        print(messages.prefix + messages.space + color.RED + messages.prsent + Fore.WHITE + messages.space + messages.enter + color.RED +messages.space + messages.fexit)
        input()
        exit()
        
        
checkinternet()


serverhost = "127.0.0.1"
serverport = 5050

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((serverhost, serverport))
cloent.sendall(bytes("Test connect", "UTF-8"))

def task():
    while True:
        in_data = client.recv(4096)
        print("От сервера: ", in_data.decode())
        
def task2():
    while True:
        out_data = str(input())
        client.sendall(bytes(out_data, "UTF-8"))
        print("Отправлено: " + out_data)
        
        
        
        
t1 = Thread(target=task2)
t2 = Thread(target=task)

t1.start()
t2.start()

t1.join()
t2.join()
