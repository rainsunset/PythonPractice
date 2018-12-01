# encoding:utf-8
language = ['Java','C','C++','.Net','Python','GO','Android','JavaScript','Html']
print(language)
print(language[0])
print(language[3].upper())
print(language[-1])
print(language[-2])
print("My first language is " + language[2].title() + " , and you ?")
language[1] = 'Vue'
print(language)
# 在末尾添加元素 返回值NONE
language.append('C')
print(language)
# 在指定索引位置插入 返回值NONE
language.insert(2,'React')
print(language)
del language[2]
print(language)
# 弹出最后一个元素 并返回元素值
print(language.pop())
print(language)
# 弹出指定索引位置元素 并返回元素值
print(language.pop(2))
print(language)
# 根据值删除元素(只删除第一个值匹配的元素) 返回值NONE
rea = 'react'
language.append(rea)
language.insert(3,rea)
print(language)
language.remove(rea)
print(language)
# 数组串联
list_a = [1,2,3] + [5,7,11]
print(list_a)
# 数组追加
list_x = [1,2,3]
list_x.extend([7,8,9])
print(list_x)
# practice
guest = ["huang xiao shan","huo ling ling","guo jia hong","liu qing yan","hou meng ying","li yu ru","tang wan"]
print("guests list : " + str(guest))
print("guest " + guest[4] + " con't come")
guest[4] = "lei xiao yan"
print("welcom name list" + str(guest))
print("now I find a bigger table , so I can banquet more guests")
guest.insert(0,"li huan")
guest.insert(4,"yang shi jun")
guest.append("li jin feng")
print("new guests list : " + str(guest))
print("table only can sit two guests")
length = len(guest)
for x in range(1,length+1):
	if (len(guest) > 2):
		print("I'm sorry "+ guest.pop().title() + " you can't come")
	else:
		print("welcom " + guest[length-x].title())
del guest[0]
del guest[0]
print("It's a null list " + str(guest))
# practice END

# 数组排序
print("Before sort " + str(language))
print(language.sort())
print("After sort " + str(language))
print(language.sort(reverse = True))
print("Sort Again " + str(language))
print(language[0])
print("sort patr time  " + str(sorted(language)))
print("sort patr time  " + str(sorted(language,reverse = True)))
print(language)
print(language.reverse())
print("After reverse" + str(language))
# practice
scenery = ["yun nan","hua shan","xi zang","tai shan","thailand"]
print(scenery)
print(sorted(scenery))
print(scenery)
print(sorted(scenery,reverse = True))
print(scenery)
scenery.reverse()
print(scenery)
scenery.reverse()
print(scenery)
scenery.sort()
print(scenery)
scenery.sort(reverse = True)
print(scenery)
# practice end

#数组切片 包括起始元素，不包括结束元素
print(scenery[1:3])
print(scenery[:4])
print(scenery[2:])
# 负数表明从后向前
print(scenery[-2:])
# 第二个买好表示 step，可以隔一个取一个
print(scenery[::2])
# 将数组颠倒的办法
print(scenery[::-1])
               
# 数组的复制
aaa = ["a1","a2"]
myaaa = aaa
print(aaa)
print(myaaa)
myaaa.append("ma1")
print(aaa)
print(myaaa)
aaa.append("a3")
print(aaa)
print(myaaa)

myscenery = scenery[:]
print(scenery)
print(myscenery)
scenery.append("bulisituo")
myscenery.append("home")
print(scenery)
print(myscenery)

# count 方法 计算元素在数组里出现的次数
results = [1,2,3,4,5,6,1,2,3,4,2,3,6,4,2,1,3,4,2,2,3,4,]
print("1在数组里出现了"+ str(results.count(1)) + "次")

# 列表解析
squares2 = [value ** 2 for value in range(1,11)]
print(squares2)
sl = ['todo1','todo2','todo9','todo10']
il = [int(_.lstrip('todo')) for _ in sl]
print(il)

numbers = list(range(2,9))
print(numbers)

# 元组
group = (12,13,14)
print(group)
print(group[0])
print(group[-1])
print(group[-2])
# group.append(15)
# group[0] = 11
for item in group:
	print(item)
group = (23,33,43)
print(group)
# 数组->元组
tuple([1,2,3,4])
tuple('string')
# 元组拆分
(a,b) = (12,13)
print(a)
print(b)
(a,b,*rest) = (1,2,3,4,5,6,7)
print(a)
print(b)
print(rest)
# 元组值替换
(a,b) = (1,2)
(b,a) = (a,b)
print(a)
print(b)