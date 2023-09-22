''' Tuple '''

"""
Mutable = Can Chance     | LIST, DICTIONARY Etc.
Unmutable = Can't Change | Tuple
"""
'''
Tuple :
t1 = ()   # Empty tuple
t1 = (1)  # Wrong way to declare a Tuple with Single element
t1 = (1)  # Tuple with Single element
print(t1) # For Output
'''

# from collections.abc import dict_items

# tuple = (1,2,3,4,5)
# print(tuple)
# print(len(tuple))
# print(tuple[:-2])


''' Printing the elements of a tuple '''
# print(t[0])

''' Cannot update the values of a tuple '''
# t[0] = 34 # throws an error

''' Creating a tuple using () '''
# t = (1, 2, 4, 5, 4, 1, 2,1 ,1)
# print(t.count(1))
# print(t.index(5))


''' Sorting Lists of Tuples '''
# d = {'a':10, 'b':1, 'c':22}
# d.items()
# dict_items([('a',10), ('b',1), ('c',22)])
# sorted(d.items())


''' like we want to swap two numbers '''
# a = 1
# b = 2
# c = a
# a = b
# b = c
# print(a,b)


''' In python we only need to write single line code for swapping '''
# a = 1
# b = 2
# a, b = b, a
# print(a,b)


a = [1, 2, "pobon", "sabbir", 5, 'wrg', 'wrg4', 'wrg3', 'wrg2', 'wrg']
_, _, _, s, *f, o, _, _ = a
print(s)
