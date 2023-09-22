''' Keyword Or Identifier '''
"""
List of the Python keywords:

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not
"""

''' Rules Of Identifiers '''
"""
1. Can't Start With A Digit
2. Can Be any length
3. Keywords Can't be Used Casually
4. Special Symbols Not Allowed
5. Can Be Combination
"""

#
#
# #********* Random Function **************
# import random
# num = random.randint(100,200)
# print(num)
#
# list1 = ["Noodles", "Riya", "Burger", "Priya"]
# a = random.choice(list1)
# print(a)
#

# assert
# a = 4
# assert a > 5, "a is smaller than 5"
# assert condition, Message
# raise AssertionError(Message)
# try:
#     num = int(input("Enter a number: "))
#     assert num % 2 == 0
# except:
#     print("Not an even number!")
# else:
#     reciprocal = 1/num
#     print(reciprocal)


'''
Keyword	        Description
and	        A logical operator
as	        To create an alias
assert	    For debugging
break	    To break out of a loop
class	    To define a class
continue	To continue to the next iteration of a loop
def	        To define a function
del	        To delete an object
elif	    Used in conditional statements, same as else if
else	    Used in conditional statements
try	        To make a try...except statement
except	    Used with exceptions, what to do when an exception occurs
False	    Boolean value, result of comparison operations
finally	    Used with exceptions, a block of code that will be executed no matter if there is an exception or not
for	        To create a for loop
from	    To import specific parts of a module
global	    To declare a global variable
if	        To make a conditional statement
import	    To import a module
in	        To check if a value is present in a list, tuple, etc.
is	        To test if two variables are equal 
lambda	    To create an anonymous function
None	    Represents a null value
nonlocal	To declare a non-local variable
not	        A logical operator
or	        A logical operator
pass	    A null statement, a statement that will do nothing
raise	    To raise an exception
return	    To exit a function and return a value
True	    Boolean value, result of comparison operations
while	    To create a while loop
with	    Used to simplify exception handling
yield	    To end a function, returns a generator
'''

# # async, await
# import asyncio
#
#
# async def main():
#     print('Hello')
#     await asyncio.sleep(5)
#     print('world')
#
#
# asyncio.run(main())
#
# # break, continue
#
# for i in range(1, 11):
#     if i == 5:
#         break
#     print(i)
#
# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(i)
#
#
# # except, raise, try
# if num == 0:
#     raise ZeroDivisionError('cannot divide')
#
#
# def except_try(num):
#     try:
#         r = 1 / num
#     except:
#         print('Exception caught')
#         return
#     return r
#
#
# print(except_try(10))
# print(except_try(0))


# lambda function'

# greet = lambda: print('Hello Lambda')
# # call lambda function
# greet()

# # lambda that accepts one argument
# greet_user = lambda name: print('Hey there,', name)
# # lambda call
# greet_user('Delilah')
