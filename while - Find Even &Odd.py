#program to find number of odd and even numbers till 100

# x = int(input("Enter a number x from 1-100   :  "))
# y = int(input("Enter a number y from 1-100  :  "))


odd = 0
even = 0


while True:
    number = int(input("Enter any number till 100 (or 0 to stop):   "))
    if number >100:
        break
    if number == 0:
        break
    if number%2==1:
        odd+=1
    else:
        even+=1
print("Total odd numbers:  ",odd)
print("Total even numbers:  ",even)
