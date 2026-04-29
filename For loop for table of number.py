#takes integer as an input 
number = int(input("Enter number you want table of:   "))

#assign value of number to var table
table=number
#you can also simply write number*mult in print arguments



for mult in range(1,11):
    
    print(number,"* ",mult,"=",table)
    #after executing 1 time the value of table will increase by "number"time
    table += number
    #table = table+number
