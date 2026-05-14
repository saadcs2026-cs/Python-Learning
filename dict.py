Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Creating a dictionary
student = {
    "name": "Saad",
    "age": 18,
    "language": "Python"
}

print(student["name"])      # Saad
print(student["age"])       # 18


#Methods


student = {"name": "Saad", "age": 18}

student["city"] = "Lahore"  # add new key
student.pop("age")          # remove key
print(student.keys())       # all keys
print(student.values())     # all values
print(student.get("name"))  # Saad