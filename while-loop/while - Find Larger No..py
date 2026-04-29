larger = -999999
x = int(input("Enter a number x   :  "))
y = int(input("Enter a number y   :  "))

while True:
    if x>y:
        larger = x
        break
    else:
        larger = y
        break
print("Larger number is:  ",larger)
