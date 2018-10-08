#encoding: utf-8
# 函数 python 是区分大小写的
# 规则: 冒号结尾 下一行的缩进视为代码块
# 约定4个空格为1个缩进  不能用tab

# for
dogs = ["lucy","li lei","hua sheng"]
for dog in dogs:
	print(str(dog) + " is a dog's name")
print("All of them are my dogs")

# 1 - 9
squares = []
for x in range(1,10):
	print (x)
	squares.append(x ** 2)
print (squares)
print (min(squares))
print (max(squares))
print (sum(squares))

squares2 = [value ** 2 for value in range(1,11)]
print(squares2)

numbers = list(range(2,9))
print(numbers)

# practice
for x in range(1,21):
	print (x)

import time
start = time.time()
# bignumber = list(range(1,1000001))
# print (bignumber)
# print(min(bignumber))
# print(max(bignumber))
# print(sum(bignumber))
print("need time " + str(time.time() - start))

oddList = range(1,20,2)
# oddList = [value * 2 -1 for value in range(1,11)]
for x in oddList:
	print (x)
threeList = range(3,31,3)
print(threeList)
# practice END

print('输入整数。。。。')
a = input()
if int(a) >= 0:
	print(a)
else:
	print(-int(a))

