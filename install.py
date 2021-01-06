import os , time

green     = '\033[92m'
cyan      = '\033[95m'
bold      = '\033[1m'
underline = '\033[4m'
end       = '\033[0m'
red       = '\033[91m'

files = ['bann/1.txt', 'bann/2.txt', 'bann/3.txt', 'bann/4.txt', 'bann/5.txt', 'bann/6.txt', 'bann/7.txt']
frames = []

os.system('cls||clear')
for name in files:
    with open(name, 'r', encoding='utf8') as f:
        frames.append(f.readlines())
for i in range(2):
    for frame in frames:
        print(''.join(frame))
        time.sleep(0.2)
        os.system('cls||clear')


print("██╗  ██╗ █████╗ ██████╗  █████╗     ██████╗  ██████╗ ██╗  ██╗ ██████╗ █████╗")
print("██║ ██╔╝██╔══██╗██╔══██╗██╔══██╗    ██╔══██╗██╔═══██╗██║  ██║██╔════╝██╔══██╗")
print("█████╔╝ ███████║██████╔╝███████║    ██████╔╝██║   ██║███████║██║     ███████║")
print("██╔═██╗ ██╔══██║██╔══██╗██╔══██║    ██╔══██╗██║   ██║██╔══██║██║     ██╔══██║")
print("██║  ██╗██║  ██║██║  ██║██║  ██║    ██████╔╝╚██████╔╝██║  ██║╚██████╗██║  ██║")
print("═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝")
print()
print(f"{bold}{red}                                  BY{end}")
print(f"{bold}{red}                    Akhmedov Lachin / Tairov Aziz{end}")
print()

print(f"{bold}{green}[1]-Kara Yilan{end}")
print(f"{bold}{green}[2]-SMS Bomber{end}")
print(f"{bold}{green}[3]-WhatsApp Bomber{end}")
print(f"{bold}{green}[4]-Instagram Bruter{end}")



if not os.path.isdir("bohca"):
     os.mkdir("bohca")
os.chdir("bohca")

#a = int(input())
a = input(f'''{bold}Enter Number:{end}''')
if '1' in a:
	os.system("git clone https://github.com/donlachin/yilan.git")
	os.chdir("yilan")
	os.system("./yilan.sh")
if '2' in a:
	os.system("git clone https://github.com/Aziz961/booms.git")
	os.chdir("booms")
	os.system("python3 bomb.py")
if '3' in a:
	os.system("git clone https://github.com/Aziz961/WBomb.git")
	os.chdir("WBomb")
	os.system("python3 wbomb.py")
if '4' in a:
	os.system("git clone https://github.com/donlachin/insta.git")
	os.chdir("insta")
	u=input("Enter uermane:")
	l=input("Enter List:")
	m=input("Enter mode:")
	os.system(f'python3 instagram.py {u} {l} -m {m}')
