''' Dictionary '''

'''
Dictionary in Python is a collection of keys values, used to store data values like a map, which, unlike other data
        types which hold only a single value as an element.
        
In Python Dictionary holds key:value pair
'''

# d1 = {}
# print(type (d1))

# d2 = {"key": "value", "A": 25, "C": "age", "D": 5}
# print(d2['A'])

# d2["Ador"]["W"] ='Normal'
# print(d2["Ador"]["W"])

# del d2['C']
# print(d2)

d = {"Meera": "Noodles", "Riya": "Burger", "Priya": "Coffee", "Ador": {"M": "Shopping", "T": "Movie", "W": "Panic"}}
# print(d)

print(d['Ador']['W'])

# print(d.get("Meera"))
# d.update({'Meera': "Chocolate" })
# print(d)
# print(d.keys())


myDict = {
    "fast": "In a Quick Manner",
    "harry": "A Coder",
    "marks": [1, 2, 5],
    "anotherdict": {'harry': 'Player'},
    1: 2
}

# Dictionary Methods
# print(list(myDict.keys())) # Prints the keys of the dictionary
# print(myDict.values()) # Prints the keys of the dictionary
# print(myDict.items()) # Prints the (key, value) for all contents of the dictionary
# print(myDict)


''' Updates the dictionary by adding key-value pairs from updateDict '''
updateDict = {
    "Lovish": "Friend",
    "Divya": "Friend",
    "Shubham": "Friend",
    "harry": "A Dancer"
}

# myDict.update(updateDict)
# print(myDict)


# print(myDict.get("harry"))        # Prints value associated with key "harry"
# print(myDict["harry"])            # Prints value associated with key "harry"


# The difference between .get and [] syntax in Dictionaries?
# print(myDict.get("harry2"))       # Returns None as harry2 is not present in the dictionary
# print(myDict["harry2"])           # throws an error as harry2 is not present in the dictionary


# student = dict()
# n = int(input("How many item in there?"))
# for i in range(n):
#     key = input("name")
#     fvrt = input("favourite food: ")
#     student[key] = fvrt
# print(student)


# student = dict()
# n = int(input("How many student in there?"))
# for i in range(n):
#     key = input("name")
#     marks = []
#     total_marks = 0
#     for j in range(3): # for 5 subject
#         num = int(input(f"Enter {j+1} subject mark: "))
#         marks.append(num)
#         total_marks += num
#     prin = ["Total Marks: ", total_marks]
#     marks.append(prin)
#     student[key] = marks
# print(student)


# a = input("Do you want to search for a student? y/n")
# s = a.lower()
# if s == 'y':
#     name = input("Enter Student Name: ")
#     if name in student.keys():
#         print(student[name])
#
#     else:
#         print("No student available with this name")
#
