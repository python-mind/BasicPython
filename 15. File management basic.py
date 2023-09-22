#  FILE IO BASICS
# "p" - open file for reading - default mode
# "W" - open file for writing
# "X" - creates file if not exists
# "a" - add more content to a file
# "t" - text mode - default mode
# "b" - binary mode
# "+" - read and write

# f = open("write.txt")       # rt is the default mode
# f=open("write.txt","r")   # then "rb"
# f function returns the file pointer
# content = f.read()    # f.read(3)    # use(3344)
# print(content)


# print(f.readLine())
# print(f.readLine())
# f.close()   #if you open a file then you must close the file.


# f = open("text.txt", "w")
# f.write("What do you Want to know from me.")
# f.close()


# f = open("text.txt", "r+")
# print(f.read())
# f.write(input("Input Anything you Want to Add: "))
# print(f.read())
# f.close()