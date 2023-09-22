"""*************** For Loop ***************"""

'''Example 1: For loop with Range Function Example'''
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for i in range(0, 10, 1):
#     print(i, end=" ")
#
# for i in range(1, 11, 2):  # 5 - 1,3,5,7,9
#     print(i, ' ', a)

'''Example 2: Print any list with for loop'''
# a = [1,2,3,4,5,6,7,8,9]
#
# for i in a:
#     print(i)
# else:
#     print("List of number is successfully inserted.")

# list1 = ["A", "B" , "C"]
# print(list1)
# for item in list1:
#     print(item)    # end = ""

'''Example 3: Ignore anytype of data from list'''
item = ["Car", "House", "Horse", "Bike"]
# for i in item:
#     if i != "Horse":
#         print(i)


'''Example 4: 2D list'''
# list2 = [["A", 3], ["B", 5] , ["C",7]]

# for item, vlu in list2:
#     print(item , vlu)


'''Example 5: Multiplication Of A Number'''
# num = int(input("Enter the number"))
# for i in range(1, 11):
#     print(str(num)+" X "+str(i) + " = " + str(i*num))
#     # print(f"{num}X{i}={num*i}")


"""*************** While Loop ***************"""
'''Example 6: While loop'''
# a = 0
# while a <45:
#     print(a, end = ' ')
#     a +=1


"""*************** Break / Continue ***************"""
'''Example 7: '''
# i = 0
# while True:
#     print(i+1 , end = " ")
#     if i == 44):
#         break               # Loop Will stop here if i == 44
#     i = i+1


'''Example 8: '''
# i = 0
# while True:
#     if (i+1) < 5:
#         i = i+1
#         continue
#
#     print(i + 1, end=" ")
#    if i == 44):
#       break               # Loop Will stop here if i == 44
#       i = i+1
