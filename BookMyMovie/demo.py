# class Solution(object):
#     def twoSum(self, nums, target):
#         for i in range(0,len(nums)):
#             index1 = i
#             for j in range(index1+1,len(nums)):
#                 sum = nums[index1] + nums[j]
#
#                 if sum == target:
#                     i1 = index1
#                     i2 = j
#                     l1 = [i1,i2]
#                     return l1
#
# obj = Solution()
# res = obj.twoSum([3,3],6)
# print(res)
# class Solution(object):
#     def addTwoNumbers(self,l1,l2):
#         # l1 = [9,9,9,9,9,9,9]
#         # l2 = [9,9,9,9]
#         # l1 = [2,4,3]
#         # l2 = [5,6,4]
#         str1 = ''
#         str2 = ''
#         # for val in l1[::-1]:
#         #     str1 = str1 + str(val)
#         #
#         # for val in l2[::-1]:
#         #     str2 = str2 + str(val)
#         l1.reverse()
#         l2.reverse()
#         for val in l1:
#             str1 = str1 + str(val)
#
#         for val in l2:
#             str2 = str2 + str(val)
#         l3 = list(str1)
#         l4 = list(str2)
#
#         if len(l3) > len(l4):
#             sub = len(l3) - len(l4)
#             for i in range(sub):
#                 l4.append(0)
#
#
#         l5 = []
#         carry = 0
#         for i in range(len(l3)):
#             val1 = int(l3[i])
#             val2 = int(l4[i])
#             res1 = val1 + val2 + carry
#             carry = 0
#             if res1 >= 10:
#                 res2 = str(res1)
#                 val3 = int(res2[1])
#                 carry = int(res2[0])
#                 l5.append(val3)
#             else:
#                 l5.append(res1)
#         else:
#             if carry > 0:
#                 l5.append(carry)
#
#         print(l5)
# obj = Solution()
# l1 = [9,9,9,9,9,9,9]
# l2 = [9,9,9,9]
# obj.addTwoNumbers(l1,l2)




# l = ['id12','id10','id2']
# print(sorted(l,key = lambda x:int(x[2:])))

# d = {"python":3,"java":1,"django":10}
# print(sorted(d.items(),key = lambda x:x[1]))

# l1 = [[1,2,3,4],[1,2]]
# res = list(map(sum,l1))
# print(res)

# a = {1,2,3,4}
# b = {1,2,5,6}
# res = a.intersection(b)
# print(res)

# input_list_1 = list(map(int,input().split())) #readonly
# input_list_2 = list(map(int,input().split()))
#
# s1 = set(input_list_1)
# s2 = set(input_list_2)
# s3 = s1.intersection(s2)
# res = list(s3)
# print(res.sort())


# l = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#
# l1 = lambda x:True if(len(x) == 6) else False
# f1 = filter(l1,l)
# print(list(f1))

# s = "str"
# r = reversed(s)
# print()

# class Human:
#     def __init__(self,sname,sgender):
#         self.name = sname
#         self.gender = sgender
#         print(self.name+" "+self.gender)
#
# obj1 = Human("syed","male")
# obj2 = Human("bob","male")


# def demo(n):
#     return 1 ,2 ,3
#
# data= demo(2)
# print(data)
# for x in range(1,10,3):
#     print(x)
# for x in range(10):
#     for y in range(x):
#         print(y)


# for x in range(1,107,20):
#     print("{:>2.3f}c how".format(x/3))



# s = "hey are what are u doin what are"
# print(s.index('are'))
# print(s.rindex("are"))



# l = [100,102,104]
# l.reverse()
# l2 = ["nnn"]
# # l3 = l2.extend(l)
# l2.extend(l)
# print(l2)
# # s = "N"
# print(s.isdigit())
# s = "123 North back"
# r = s.split(" ")
# print(r)

# add_one = lambda x:x+1
# print(add_one(7))
# nums = [3,5,16,27]
# some_nums = list(filter(lambda num: num <10,nums))
# print(some_nums)

# func = lambda x:  x
# print(func(2))
# res = list(map(lambda x:x+1,[1,2,3]))
# print(res)
# l = [1,2,"hey"]
# print(l[2])
# x = 12
# def f1():
#     global x
#     x+=1
#     print(x)
# f1()
# print("x")


# def f1(a,b=[]):
#     b.append(a)
#     return b
# print(f1(2,[3,4]))

# def f(x):
#     print("Outer")
#     def f1(a):
#         print("inner")
#         print(a,x)
#
# f(3)
# f1(1)

# def check_even_odd(**check):
#     if check['is_Even'] % 2 == 0:
#         print('Even')
#     else:
#         print("Odd")
#
# check_even_odd(is_Even=3)


# if(1,2):
#     print('foo')
# x =10
# y = 3
# if x < y: print('foo')
# else: print('bar')

# print(64//2)
# print(1000<300)

# a = (1,2,3)
# b = (1,2,3)
# print(a is b)

x = 0
for i in range(10):
    print(i)

