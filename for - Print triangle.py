#program to print a right triangle on 'n' number of rows

n = int(input("Enter a number:  "))

r = 1 #take row =1 to start with 1 star in row 1

for x in range(n):
    
    print("*"*r)
    r+=1

