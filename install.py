import os , time

green      = '\033[92m'
cyan       = '\033[95m'
bold       = '\033[1m'
underline  = '\033[4m'
end        = '\033[0m'
black 	   = "\033[0;30m"
red        = '\033[91m'
brown      = "\033[0;33m"
DARK_GRAY  = "\033[1;30m"
LIGHT_GRAY = "\033[0;37m"
FAINT      = "\033[2m"
ITALIC     = "\033[3m"
BLINK      = "\033[5m"
NEGATIVE   = "\033[7m"
CROSSED    = "\033[9m"
PURPLE     = "\033[0;35m"

#files = ['bann/1.txt', 'bann/2.txt', 'bann/3.txt', 'bann/4.txt', 'bann/5.txt', 'bann/6.txt', 'bann/7.txt']
#frames = []

#os.system('cls||clear')
#for name in files:
#    with open(name, 'r', encoding='utf8') as f:
#        frames.append(f.readlines())
#for i in range(2):
#    for frame in frames:
#        print(''.join(frame))
#        time.sleep(0.2)
#        os.system('cls||clear')


print(f"""{ITALIC}
       ▄█   ▄█▄    ▄████████    ▄████████    ▄████████      
      ███ ▄███▀   ███    ███   ███    ███   ███    ███         
      ███▐██▀     ███    ███   ███    ███   ███    ███         
     ▄█████▀      ███    ███  ▄███▄▄▄▄██▀   ███    ███        
    ▀▀█████▄    ▀███████████ ▀▀███▀▀▀▀▀   ▀███████████      
      ███▐██▄     ███    ███ ▀███████████   ███    ███        
      ███ ▀███▄   ███    ███   ███    ███   ███    ███        
      ███   ▀█▀   ███    █▀    ███    ███   ███    █▀       
      ▀                        ███    ███                 
                                                                
▀█████████▄  ▄██████▄     ▄█    █▄     ▄████████    ▄████████ 
 ███    ███ ███    ███   ███    ███   ███    ███   ███    ███ 
 ███    ███ ███    ███   ███    ███   ███    ███   ███    ███
 ███    ███ ███    ███   ███    ███   ███    █▀    ███    ███
▄███▄▄▄██▀  ███    ███  ▄███▄▄▄▄███▄▄ ███          ███    ███
▀███▀▀▀██▄  ███    ███ ▀▀███▀▀▀▀███▀  ███        ▀███████████ 
 ███    ██▄ ███    ███   ███    ███   ███    █▄    ███    ███ 
 ███    ███ ███    ███   ███    ███   ███    ███   ███    ███ 
▄█████████▀  ▀██████▀    ███    █▀    ████████▀    ███    █▀   {end}""")
print()
print(f"""{bold}{red}{BLINK}                             BY 
	       Akhmedov Lachin / Tairov Aziz{end}""")
print()

print(f"{bold}{green}[1]-Kara Yilan{end}")
print(f"{bold}{green}[2]-SMS Bomber{end}")
print(f"{bold}{green}[3]-WhatsApp Bomber{end}")
print(f"{bold}{green}[4]-Instagram Bruter{end}")

print(f"{ITALIC}'* r' - reinstall{end}")
print(f"{ITALIC}'ref' - refresh Kara Bohca{end}")



if not os.path.isdir("bohca"):
     os.mkdir("bohca")
os.chdir("bohca")

while True:
	a = input(f'''{bold}Enter Number:{end}''')
	if a=="ref":
		os.chdir('..//..')
		os.system("rm -rf kara_bohca/")
		os.system("git clone https://github.com/Aziz961/kara_bohca.git")
		os.chdir("kara_bohca")
		os.system("python3 install.py")
	elif a=="1":
		os.system("git clone https://github.com/donlachin/yilan.git")
		os.chdir("yilan")
		os.system("./yilan.sh")
	elif a=="1 r":
		os.system("rm -rf yilan/")
		os.system("git clone https://github.com/donlachin/yilan.git")
		os.chdir("yilan")
		os.system("./yilan.sh")
	elif a=="2":
		os.system("git clone https://github.com/Aziz961/booms.git")
		os.chdir("booms")
		os.system("python3 bomb.py")
	elif a=="2 r":
		os.system("rm -rf booms/")
		os.system("git clone https://github.com/Aziz961/booms.git")
		os.chdir("booms")
		os.system("python3 bomb.py")
	elif a=="3":
		os.system("git clone https://github.com/Aziz961/WBomb.git")
		os.chdir("WBomb")
		os.system("python3 wbomb.py")
	elif a=="3 r":
		os.system("rm -rf WBomb")
		os.system("git clone https://github.com/Aziz961/WBomb.git")
		os.chdir("WBomb")
		os.system("python3 wbomb.py")
	elif a=="4":
		os.system("git clone https://github.com/donlachin/insta.git")
		os.chdir("insta")
		u=input("Enter uermane:")
		l=input("Enter List:")
		m=input("Enter mode:")
		os.system(f'python3 instagram.py {u} {l} -m {m}')
	elif a=="4 r":
		os.system("rm -rf insta")
		os.system("git clone https://github.com/donlachin/insta.git")
		os.chdir("insta")
		u = input("Enter uermane:")
		l = input("Enter List:")
		m = input("Enter mode:")
		os.system(f'python3 instagram.py {u} {l} -m {m}')
		break
	else:
		print(f"{bold}{red}Invalid command{end}")


