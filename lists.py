Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Creating a list
fruits = ["apple", "banana", "mango"]
numbers = [1, 2, 3, 4, 5]
mixed = ["Saad", 18, True, 3.14]


# Accessing items
print(fruits[0])   # apple
print(fruits[-1])  # mango
Slide 3 — Useful operations
pythonfruits = ["apple", "banana", "mango"]



print(len(fruits))      # 3
print(fruits[1:3])      # ['banana', 'mango']
print("apple" in fruits) # True



#Adding/Removing
fruits = ["apple", "banana"]

fruits.append("mango")   # adds to end
fruits.insert(1, "kiwi") # adds at position
fruits.remove("apple")   # removes by value
fruits.pop()             # removes last item


#Sorting/Counting
numbers = [3, 1, 4, 1, 5, 2]

numbers.sort()           # [1,1,2,3,4,5]
numbers.reverse()        # reverses list
numbers.count(1)         # 2 (counts 1s)
numbers.index(4)         # finds position


#Other useful methods
pythona = [1, 2, 3]
b = [4, 5, 6]

a.extend(b)    # [1,2,3,4,5,6]
a.copy()       # makes a copy
a.clear()      # empties list
len(a)         # counts items


#Looping through a List
fruits = ["apple", "banana", "mango"]

# Loop through list
for fruit in fruits:
    print(fruit)

