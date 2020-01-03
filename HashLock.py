#HashLock By: Kat9_123
import hashlib
from os import system
system("title "+"HashLock, V1.2, By: Kat9_123")
system("mode con: cols=75 lines=10")
print(" 			  ####################")
print(" 			  ## HashLock, V1.2 ##")
print(" 			  ####################")
print("")

salt = "ADZGICDFPW"

password = input("Enter your master password: ")

while True:
	system("cls")
	print(" 			  ####################")
	print(" 			  ## HashLock, V1.2 ##")
	print(" 			  ####################")
	print("")
	service = input("Service: ")
	if service == "":
		exit()
	service = service.upper()
	print("")
	temp = password + service + salt
	hashed = hashlib.sha256(temp.encode()).hexdigest()
	print("Password: " + hashed)

	input("")