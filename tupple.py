Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Creating a tuple
person = ("Saad", 18, "Python")


# Accessing items
print(person[0])    # Saad
print(person[-1])   # Python
print(len(person))  # 3


#List vs Tuple


# List — changeable ✅
fruits = ["apple", "banana"]
fruits[0] = "mango"  # works!


# Tuple — unchangeable ❌
fruits = ("apple", "banana")
fruits[0] = "mango"  # ERROR!