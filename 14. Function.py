''' Function '''

'''
Type of Function - 1. Perform a task  2. return a value
'''
'''
Function Procedure:

*   'def'        : Indicate a function 
*   functionName : Function Name 
*   Parameter    : required Value to execute the procedure
*   Return       : return is used to get the expected result from the function

def functionName(parameter):   
    Function Procedure....
    
    return 
'''

'''Example 1: '''
# def welcome():
#     print("hello it's an example of performing a task.")

# welcome()   # Calling the function

'''Example 2: '''
# def you(name):
#     print("it is an example of performing task. ")
#     print(f'Hey {name}. How are you?')
# you('Piku')

'''Example 3: '''
# a = 2
# b = 9
# c = sum((a , b))          # builtin Function
# print(c)

# def sub(a, b):
#     return "A is big" if a > b else "b is big"
# print(sub(5, 8))

'''Example 4: '''
# a = 2
# b = 9
# def function(a, b):  # Function Declaration
#     print(f" Substitution of {a} & {b} is ", b - a)
#     return b - a

# function(a, b)              # Calling Function
# print(function(a, b))

'''Example 5: '''
# def fun1(a,b):
#     """Doc String Example(" We will find this text if we use __doc__ with function dot.")"""
#     multiply = a*b
#     print(multiply)
#     return multiply

# s = fun1(a, b)              # Calling Function
# print(s)
# print(fun1 . __doc__)

'''Example 6: '''
# def percent(marks):
#     p = ((marks[0] + marks[1] + marks[2]+ marks[3])/400 )*100
#     return p
#
# marks1 = [45, 78, 86, 77]
# percentage1 = percent(marks1)
#
# marks2 = [75, 98, 88, 78]
# percentage2 = percent(marks2)
# print(percentage1, percentage2)

'''Example 7: '''
# def greet(name=input("Stranger")):
#     print("Good Day, " + name)
# greet()

'''**************Lamda Function***********'''

# def minus( x , y):
#     return x - y
# minus = lambda x, y: x-y
# print(minus(9, 4))


'''Example 8: '''
# def a_first(a):
#     return a[2]
# a = [[1, 42, 56], [9,6, 5], [8,23,9]]
# a.sort(key = a_first)

# a = [[1, 42, 56], [9,6, 5], [8,23,9]]
# a.sort(key=lambda x:x[1])
# print(a)

''' Enumerate Function '''
# normal:
# a = ["Car" , "House", "Horse", "Bike"]

# b= 1
# for item in a:
#     if b%2 == 0:
#         print(f"I've {item}. ")   #end = ""
#     b += 1


''' Enumerate Function '''
# for index, item in enumerate(a):
#     if index % 2 == 0:
#         print(f"I've {item}. ")


''' Join Function: '''
# normal:
# for item in a:
#     print(item, "and", end = " ")

# # Join with function: '''
# s = ",".join(a)
# print(s)


''' xargs(*) use to Accept all the Single type parameter for the function'''

# def add(*num):
#     print(num)
#     sum = 0
#     for i in num:
#         sum += i
#     return sum
# print(add(10, 1, 5))


'''Example 2: xxargs(**) is used to Accept all the parameter with value and key for the function     ** == Dictionary'''
# def user_details(**user):
#     print(user)
# user_details(id=1, name='John', age=22)
