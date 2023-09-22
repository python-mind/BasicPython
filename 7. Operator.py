import variable

''' Operator '''
"""
Logical Operators:
and : Returns True if both statements are true	x < 5 and  x < 10	
or	: Returns True if one of the statements is true	x < 5 or x < 4	
not	: Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

Identity Operators:
is 	    : Returns True if both variables are the same object	x is y	
is not	: Returns True if both variables are not the same object	x is not y

Membership Operators:
in      :      True if value is found in the sequence
not in  :      True if value is not found in the sequence

Comparison Operation
==  :  Equal       |  If A == B: ( if A equal to B)
!=  :  Not Equal   |  If A == B: ( if A not equal to B)
>=  :  Greater or Equal 
<=  :  Less or Equal
>   :  Greater
<   :  Smaller / less then

Arithmetic Common Operator
+  : Sum
-  : Subtract
*  : Multiply
/  : Divide
%  : Modulus/ ভাগ শেষ
** : Exponentiation/বর্গ
// : Floor Division/ ভাগ ফল

Assignment Operator:
=	 :   x = 5    :	x = 5	
+=	 :   x += 3   :	x = x + 3	
-=	 :   x -= 3   :	x = x - 3	
*=	 :   x *= 3   :	x = x * 3	
/=	 :   x /= 3   :	x = x / 3	
%=	 :   x %= 3   :	x = x % 3	
//=	 :   x //= 3  :	x = x // 3	
**=	 :   x **= 3  :	x = x ** 3	
&=	 :   x &= 3   :	x = x & 3	
|=	 :   x |= 3   :	x = x | 3	
^=	 :   x ^= 3   :	x = x ^ 3	
>>=	 :   x >>= 3  :	x = x >> 3	
<<=	 :   x <<= 3  :	x = x << 3

Bitwise Operators:
&  :	AND :	Sets each bit to 1 if both bits are 1           :	x & y	
|  :	OR  :	Sets each bit to 1 if one of two bits is 1      :	x | y	
^  :	XOR	:   Sets each bit to 1 if only one of two bits is 1 :	x ^ y	
~  :	NOT	:   Inverts all the bits	                        :   ~x	
<< :	Left shift  :	Shift left by pushing zeros in from the right and let the leftmost bits fall off    :	x << 2	
>> :	right shift :	Shift right by pushing copies of the leftmost bit in from the left,                 :   x >> 2
                        and let the rightmost bits fall off	
                        
"""
# Example:

''' Examples of Arithmetic Operator '''
# let us take a variable with a value.
#
# a = 9
# b = 4
#
# # Addition of numbers
# add = a + b
#
# # Subtraction of numbers
# sub = a - b
#
# # Multiplication of number
# mul = a * b
#
# # Division(float) of number
# div1 = a / b
#
# # Division(floor) of number
# div2 = a // b
#
# # Modulo of both number
# mod = a % b
#
# # Power
# p = a ** b
#
# # print results
# print(add)
# print(sub)
# print(mul)
# print(div1)
# print(div2)
# print(mod)
# print(p)

''' Examples of Relational Operators '''
#
# a = 13
# b = 33
#
# # a > b is False
# print(a > b)
#
# # a < b is True
# print(a < b)
#
# # a == b is False
# print(a == b)
#
# # a != b is True
# print(a != b)
#
# # a >= b is False
# print(a >= b)
#
# # a <= b is True
# print(a <= b)


''' Examples of Assignment Operators '''
# a = 10
#
# # Assign value
# b = a
# print(b)
#
# # Add and assign value
# b += a
# print(b)
#
# # Subtract and assign value
# b -= a
# print(b)
#
# # multiply and assign
# b *= a
# print(b)
#
# # bitwise lishift operator
# b <<= a
# print(b)

''' Membership operator '''
# x = 24
# y = 20
# list = [10, 20, 30, 40, 50]
#
# if (x not in list):
#     print("x is NOT present in given list")
# else:
#     print("x is present in given list")
#
# if (y in list):
#     print("y is present in given list")
# else:
#     print("y is NOT present in given list")


''' Examples of Operator Associativity '''

'''
Left-right associativity: 
100 / 10 * 10 is calculated as (100 / 10) * 10 | not as 100 / (10 * 10)
'''
print(100 / 10 * 10)

'''
Left-right associativity:
5 - 2 + 3 is calculated as (5 - 2) + 3 and not as 5 - (2 + 3)
'''
print(5 - 2 + 3)

'''
right-left associativity:
2 ** 3 ** 2 is calculated as 2 ** (3 ** 2) and not as (2 ** 3) ** 2
'''
print(2 ** 3 ** 2)
