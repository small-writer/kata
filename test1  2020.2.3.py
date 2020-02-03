#给你一个整数n. 从 1 到 n 按照下面的规则打印每个数：
# 如果这个数被3整除，打印fizz.
# 如果这个数被5整除，打印buzz.
# 如果这个数能同时被3和5整除，打印fizz buzz.

num=int(input('n='))
result=[]
i=1
while i<=num:
    if i % 3 != 0 and i % 5 != 0:
        result.append(i)
    elif i%3==0 and i%5==0:
        result.append('fizz buzz')
    elif i%3==0:
        result.append('fizz')
    else:
        result.append('buzz')
    i+=1
print(result)