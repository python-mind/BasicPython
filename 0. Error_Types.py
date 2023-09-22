
"""
There are 3 Types of Error. 
LOGICAL , SYNTAX & RUN TIME Errors.

Logical Error: A mistake in a program's source code that results in an incorrect or unexpected behavior.

Syntax Error: A syntax error occurs when a programmer writes an invalid statement. such as spelling & punctuation
                errors, incorrect labels.
 
Run-time  Error: A runtime error is a type of error that occurs during program execution. The Python interpreter  
                    executes a script if it is syntactically correct. However, if it encounters an issue at runtime,
                    which is not detected when the script is parsed, script execution may halt unexpectedly.
"""

''' 
Logical errors – also called semantic errors, logical errors cause the program to behave incorrectly, but they do not
                 usually crash the program. Unlike a program with syntax errors, a program with logic errors can be run, 
                 but it does not operate as intended.
'''

''' Example of those Error '''

''' Syntax Error: Unterminated String Literal'''
# print("Let's get some Error Example.)

#
''' Syntax Error: unmatched'''
a = 2
b = 4
if a > b:
    print('a- Big)   # ' is missing
else:
    print("b- Big")


''' runtime Error: '''
print(3/0)  # Division by Zero


''' Semantic Error: unexpected output, Wrong Logic '''
a = 20            # Logical Error
b = 10            # Wrong Output: ---> a + b / 3 == 20 + (10/2) == 25
print(a+b/3)      # Correct Output: -> (a + b) / 3 == (20 + 10) / 2 == 15


''' Type Error: '''
a = 10      # Integer Type
b = "20"    # String Type
print(a+b)  # Output: Type Error


''' Name Error: '''
A = 10
rst = A + B       # No value for B
print(rst)


''' Value Error:'''
a = "Hello"
print(int(a))


''' Indentation Error '''
a = "Hello"     # There is some space
    print(a)    # before Print Function



''' list index Error '''
a = [1,2,3,4,5]  # index number of 5 is: 4
print(a[5])      # Calling for index 6 value: Out of index Error



