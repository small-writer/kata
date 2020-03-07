#给定一个无序的数组，将其进行排序

import random
list=list(range(10))
random.shuffle(list)
print(list)

#冒泡

for i in range(len(list)-1):
    for j in range(len(list)-1):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]

print(list)


#插入

for i in range(1, len(list)):
    value = list[i]
    for j in range(i-1,-1,-1):
        if list[j] < value:
            list[j+1]=list[j]
            list[j]=value
print(list)
