''' String Function '''

my_str = "subscribe fun with data science"

# print(my_str.isalnum())                # If No Space in sentence.
# print(my_str.endswith("science"))      # If End with "Input"
# print(my_str.startswith('Subscribe'))  # If Start with "Input"
# print(my_str.count("s"))               # Count the total presence of "Input"
# print(my_str.capitalize())             # Helps to capitalize the first String
# print(my_str.find("data"))             # It tells the index number
# print(("data") in my_str)              # Check if "input" in a string
# print(my_str.lower())                  # Helps to smallerize the String
# print(my_str.upper())                  # Helps to capitalize the String

# story = "Harry is good.\nHe\tis ve\\ry good"
# print(story)

'''Convert negative number to positive with function - abs() -'''
"""
STRING SLICING :

1. String slicing is obtaining a sub-string from a string
2. Slicing starts with the first index and ends at the last index

Str:    We'll
index: "0,1,2,3,4.....n-1"
       "W,e,',l,l..... , ."

"""
''' String Slicing '''
my_str = "We'll Learn about String Slicing."

# print(len(my_str))
# print(my_str[1:9])
# print(my_str[0:9])
# # print(my_str[0:33])
# print(my_str[0:65])
# print(my_str[0:33:2])         # skips one-one character
# # print(my_str[:33])          # it will take whole length
# print (my_str[:5])            # it will take from zero till
# print(my_str[::2])            # By default, take as [0:33:1] 24 is length of string


''' FOR NEGATIVE INDICES '''

# my_str = "Anika is a good girl"

# print(my_str[-4:-2])        # can also write as [29:31] in positive
# print(my_str[20:22])
# print(my_str[20:22])
# print(my_str[::-1])         # it will reverse the string


''' Special Example '''
letter = '''Dear |NAME|,
Greetings from ABC coding house. I'm happy to tell you about your selection
You are selected!
Have a great day ahead!
Thanks and regards,
Bill
Date: <|DATE|>
'''

# name = input("Enter Your Name: ")
# date = input("Enter Date: ")
# letter = letter.replace("|NAME|", name)
# letter = letter.replace("<|DATE|>", date)
# print(letter)

'''  '''
x = "Hi!"
y = "My name is Aquib"
z = x + y

# print(z)
# print()
# print(y[len(y) - 5])
# print(ord(y[-1]))
# print(sorted(z))

str = "***** This is string example....wow!!! *****"
print(str.strip())
print(str.strip().title())
