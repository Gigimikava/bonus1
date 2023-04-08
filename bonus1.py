# #n1
# from math import sqrt
# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def __str__(self):
#         return f"{self.x} , {self.y}"
#     def __add__(self, other):
#         return sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
# a=Point(10,15)
# b=Point(7,1)
# print(a.__add__(b))


#n3
# s = input("Put Roman Number: ")
# def roman_to_integer(s):
#         nums = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
#         x = 0
#         for i in range(len(s)):
#             if i+1 != len(s) and nums[s[i]] < nums[s[i+1]]:
#                 x = x - nums[s[i]]
#             else:
#                 x = x + nums[s[i]]
#         return x
# print(roman_to_integer(s))









