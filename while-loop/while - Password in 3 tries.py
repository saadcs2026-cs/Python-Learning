#Suspend account on wrong password

password = "saad212006"

enter = input("Enter your Password(You have 3 tries):  ")
take = 2
while True:
    if take == 0:
        print("Wrong Password! Accout Suspended")
        break
    if enter == password:
        print("Correct Password!")
        break
    else:
        print("Incorrect Password!\n",take," TRIES LEFT!")
        take-=1
        enter = input("Enter your Password:  ")
