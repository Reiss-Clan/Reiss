import socket
import sys
import os
from time import sleep
import random
from replit import db
db["key"] = "value"
value = db["key"]
del db["key"]
keys = db.keys()
matches = db.prefix("prefix")
os.system("clear")
red="\033[31m"
green="\033[32m"
yellow="\033[33m"
blue="\033[34m"
purple="\033[35m"
cyan="\033[36m"
white="\033[37m"
ksmk=0
print(red,"""
     __/)     (\__
  ,-'~~(   _   )~~`-.
 /      \/'_`\/      \
|       /_(_)_\       |
|     _(/(\_/)\)_     |
|    / // \ / \\ \    |
 \  | ``  / \ ''  |  /
  \  )   /   \   (  /
   )/   /     \   \(
   '    `-`-'-'    `
""")
print(green,
""".d8888.  .d88b.   .o88b. db   dD d88888b d888888b     
88'  YP .8P  Y8. d8P  Y8 88 ,8P' 88'     `~~88~~'     
`8bo.   88    88 8P      88,8P   88ooooo    88        
 `Y8b. 88    88 8b      88`8b   88~~~~~    88        
db   8D `8b  d8' Y8b  d8 88 `88. 88.        88        
`8888Y'  `Y88P'   `Y88P' YP   YD Y88888P    YP   
""")


portlist=[1, 7, 9, 11, 13, 15, 17, 18, 19, 20, 21, 22, 23, 25, 37, 39, 42, 43, 49, 50, 53, 57, 65, 67, 68, 69, 70, 77, 79, 80, 87, 88, 95, 98, 101, 102, 104, 105, 106, 107, 109, 110, 111, 113, 115, 117, 119, 123, 129, 135, 137, 138, 139, 143, 161, 162, 163, 164, 174, 177, 178, 179, 191, 194, 199, 201, 202, 204, 206, 209, 210, 213, 220, 345, 346, 347, 369, 370, 371, 372, 389, 406, 427, 443, 444, 445, 464, 465, 487, 500, 512, 513, 514, 515, 517, 518, 520, 525, 526, 530, 531, 532, 533, 538, 540, 543, 544, 546, 547, 548, 549, 554, 556, 563, 587, 607, 610, 611, 612, 628, 631, 636, 655, 706, 749, 750, 751, 752, 754, 760, 765, 775, 777, 779, 783, 808, 871, 873, 901, 989, 990, 992, 993, 994, 995, 1001, 1080, 1093, 1094, 1099, 1109, 1127, 1178, 1194, 1210, 1214, 1236, 1241, 1300, 1313, 1314, 1352, 1433, 1434, 1524, 1525, 1529, 1645, 1646, 1649, 1677, 1701, 1812, 1813, 1863, 1957, 1958, 1959, 2000, 2003, 2010, 2049, 2053, 2086, 2101, 2102, 2103, 2104, 2105, 2111, 2119, 2121, 2135, 2150, 2401, 2430, 2431, 2432, 2433, 2583, 2600, 2601, 2602, 2603, 2604, 2605, 2606, 2607, 2608, 2628, 2792, 2811, 2947, 2988, 2989, 3050, 3130, 3306, 3493, 3632, 3689, 3690, 4031, 4094, 4190, 4224, 4353, 4369, 4373, 4557, 4559, 4569, 4600, 4691, 4899, 4949, 5002, 5050, 5051, 5052, 5060, 5061, 5151, 5190, 5222, 5269, 5308, 5353, 5354, 5355, 5432, 5555, 5556, 5666, 5667, 5672, 5674, 5675, 5680, 5688, 6000, 6001, 6002, 6003, 6004, 6005, 6006, 6007, 6346, 6347, 6444, 6445, 6446, 6566, 6667, 7000, 7001, 7002, 7003, 7004, 7005, 7006, 7007, 7008, 7009, 7100, 8021, 8080, 8081, 8088, 8990, 9098, 9101, 9102, 9103, 9359, 9418, 9667, 9673, 10000, 10050, 10051, 10080, 10081, 10082, 10083, 10809, 11201, 11371, 13720, 13721, 13722, 13724, 13782, 13783, 15345, 17001, 17002, 17003, 17004, 20011, 20012, 22125, 22128, 22273, 24554, 27374, 30865, 57000, 60177, 60179]
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
kk=0
def connecter():
	try:
		while True:
			port=random.choice(portlist)
			s.connect_ex((ip,port))
			l=socket.getservbyport(port)
			print(green,"done {}".format(port),l)
	except:
		
		print(red,"FUCK")
	
iii=input("ENTER HOST NAME: ")
ip=socket.gethostbyname(iii)
kk=0
while True:
	connecter()
	kk+=1
	print(green,"DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	connecter()
	kk+=1
	print("DONE [{}]".format(kk))
	
