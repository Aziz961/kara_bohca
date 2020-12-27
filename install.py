from termcolor import colored
import os , time

files = ['bann/1.txt', 'bann/2.txt', 'bann/3.txt', 'bann/4.txt', 'bann/5.txt', 'bann/6.txt', 'bann/7.txt']
frames = []

os.system('cls||clear')
for name in files:
    with open(name, 'r', encoding='utf8') as f:
        frames.append(f.readlines())
for i in range(2):
    for frame in frames:
        print(colored(''.join(frame), 'green'))
        time.sleep(0.2)
        os.system('cls||clear')


print("██╗  ██╗ █████╗ ██████╗  █████╗     ██████╗  ██████╗ ██╗  ██╗ ██████╗ █████╗")
print("██║ ██╔╝██╔══██╗██╔══██╗██╔══██╗    ██╔══██╗██╔═══██╗██║  ██║██╔════╝██╔══██╗")
print("█████╔╝ ███████║██████╔╝███████║    ██████╔╝██║   ██║███████║██║     ███████║")
print("██╔═██╗ ██╔══██║██╔══██╗██╔══██║    ██╔══██╗██║   ██║██╔══██║██║     ██╔══██║")
print("██║  ██╗██║  ██║██║  ██║██║  ██║    ██████╔╝╚██████╔╝██║  ██║╚██████╗██║  ██║")
print("═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝")
print()
print("                                BY")
print("                  Ahmedov Lachin / Tairov Aziz")
print()

print("[1]-Kara Yilan")
print("[2]-SMS Bomber")
print("[3]-WhatsApp Bomber")
print("[4]-Instagram Bruter")


os.chdir('..')
if not os.path.isdir("karabohca"):
     os.mkdir("karabohca")
os.chdir("karabohca")

a = input('''Enter Number:''')
if '1' in a:
    os.system("git clone https://github.com/donlachin/yilan.git")
if '2' in a:
    os.system("git clone https://github.com/Nikait/ni_bomber.git")
if '3' in a:
    os.system("git clone https://github.com/TAIROV1/WBomb.git")
if '4' in a:
    os.system("git clone https://github.com/donlachin/insta.git")

