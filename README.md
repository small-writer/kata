**number7/number7.py**

```python
num=input('n=')        #1次
i=1                    #1次     空间复杂度为1
if is_true(num):       #1次
    while i<=int(num): #n次
        if '7' in str(i) or i%7==0:   #1次
            print('pass')      #1次

        else:
            print(i)    #1次
        i+=1            #1次   
```

f(n)=2+n*(2+1)=3n+2  ;  T(n)=O(n)

S(n)=O(1)



**publishs/mod.py**

```python
#冒泡 正序
def bublle_sort(list):              #  空间复杂度为1
    for i in range(len(list)-1):       #n-1次
        for j in range(len(list)-1):   #n-1次
            if list[j]>list[j+1]:      #1次
                list[j],list[j+1]=list[j+1],list[j]   #2次



#插入 逆序
def insertion_sort(list):
    for i in range(1, len(list)):        #n次
        value = list[i]                  #1次     空间复杂度为1
        for j in range(i - 1, -1, -1):   #n次
            if list[j] < value:          #1次
                list[j + 1] = list[j]    #1次
                list[j] = value          #1次


#文件创建和读写
def file_accessor(filename,seq):
    f=open(filename, 'w+')
    f.write(''.join(str(i) for i in seq))
    f.close()


#输入正数
def positive_num(num):                #空间复杂度为1
    if num.isdigit() and int(num) > 0:#1次
        return True                   #1次
    else:
        print('请输入正数')             #1次    
```

bubble_sort: f(n)=3(n-1)(n-1)=3n^2-6n+3   ; T(n)=O(n^2)

​                                                                            S(n)=O(1)

insertion_sort:f(n)=n*3n=3n^2   ; T(n)=O(n^2)

​                                                            S(n)=O(1)

positive_num：f(n)=2    ; T(n)=O(1)

​                                             S(n)=O(1)

**fizzbuzz/fizzbuzz_test.py**

```python
num=input('n=')   #1次    空间复杂度为1
result=[]         #1次    空间复杂度为1
i=1               #1次    空间复杂度为1

if is_true(num):    #1次
    while True and i<=int(num): #n次          空间复杂度为n
        if i % 3 != 0 and i % 5 != 0: #1次
            result.append(i)  #1次
        elif i%3==0 and i%5==0:#1次
            result.append('fizz buzz')#1次
        elif i%3==0:             #1次 
            result.append('fizz')#1次
        else:                    #1次
            result.append('buzz')#1次
        i+=1                     #1次
    print(result)               #1次
```

f(n)=3+(n*(1+1+1+1+1)+1)=5n+1  ;  T(n)=O(n)

f(n)=2+n                                            ;  S(n)=O(n)



**file_seq/file_seq.py**

```python
import random
import publishs

def file_accessor(filename,seq):
    f=open(filename, 'w+')#1次
    f.write(','.join(str(i) for i in seq))#1次
    f.close()#1次

seq=list(range(3000))                             #1次    空间复杂度为3000
new_seq=random.sample(seq,random.randint(1,100))  #n次    空间复杂度为n

file_accessor('file',new_seq)                      #空间复杂度为n              

publishs.bublle_sort(new_seq)                     #3n^2-6n+3次
file_accessor('new_file',new_seq)                 #空间复杂度为n
```

f(n)=1+n+3+(3n^2-6n+3)+3=3n^2-5n+10    ;  T(n)=O(n^2)

f(n)=3000+3n                                                   ;   S(n)=O(n)



**num_threading/num_threading.py**

```python
import os
import threading
import random
import sys
sys.path.append('..')
from publishs import mod


#生成随机数组文件
def generate_orig(data_size,list):   
    while data_size < file_size:    #n次      
        list.append(random.randint(1, 9))#1次      空间复杂度为n
        mod.file_accessor('original_file', list)  #空间复杂度为n
        data_size = os.path.getsize('original_file')#1次
    print(os.path.getsize('original_file')) #1次   空间复杂度为1
#正序
def ascending_file():
    list1=list.copy()     #n次     空间复杂度为n
    mod.bublle_sort(list1)    #3n^2-6n+3次
    mod.file_accessor('ascend_file',list1)    #空间复杂度为n
    data_size = os.path.getsize('ascend_file')   #1次
    print(os.path.getsize('ascend_file'))    #1次   空间复杂度为1
    print('thread1 pass')     #1次     空间复杂度为1
#逆序
def descending_file():
    list2=list.copy()    #n次    空间复杂度为n
    mod.insertion_sort(list2)    #3n^2次   
    mod.file_accessor('descend_file',list2)    #空间复杂度为n
    data_size = os.path.getsize('descend_file')  #1次
    print(os.path.getsize('descend_file'))  #1次    空间复杂度为1
    print('thread2 pass')   #1次    空间复杂度为1
#多线程
def main():
    thread1=threading.Thread(target=ascending_file(),name='T1')
    thread2=threading.Thread(target=descending_file(),name='T2')
    thread1.start()
    thread2.start()
# 执行
input_size=input('请输入文件大小：')   #1次   空间复杂度为1
list = []                           #1次   空间复杂度为1→n
data_size = 0                       #1次   空间复杂度为1
if mod.positive_num(input_size):    #1次
    file_size = int(input_size)     #1次    空间复杂度为1
    generate_orig(data_size,list)   #1次
    main()                          #1次
```

f(n)=3+( 1+( 2n+1 )+( ( n+( 3n^2-6n+3)+3 )+( n+(3n^2)+3 ) ) )=6n^2-2n+14   ;   T(n)=O(n^2)

f(n)=1+n+1+(1+(2n+1)+( (2n+2)+(2n+2) ) )=7n+8                                               ;    S(n)=O(n)



**num_threading/threading_unittest.py**

```python
import sys
sys.path.append('..')
from publishs import mod
import unittest,num_threading

class TestCase(unittest.TestCase):
    def test_pos_num(self):
        self.assertEqual(type(num_threading.file_size),int)#1次
    def test_file_reader(self):
        lis = num_threading.list#1次       空间复杂度为n

        with open('original_file','r') as f1:
            lis1 = num_threading.list#1次       空间复杂度为n
            exp_org = int(''.join(str(i) for i in lis1))#1次    空间复杂度为1
            self.assertEqual(int(f1.read()),exp_org)#1次
            f1.close()#1次

        with open('ascend_file','r') as  f2:
            mod.bublle_sort(lis)#3n^2-6n+3次
            exp_asd=int(''.join(str(i) for i in lis))#1次   空间复杂度为1
            self.assertEqual(int(f2.read()), exp_asd)#1次
            f2.close()#1次

        with open('descend_file','r') as  f3:
            mod.insertion_sort(lis)#3n^2次
            exp_desd=int(''.join(str(i) for i in lis))#1次   空间复杂度为1
            self.assertEqual(int(f3.read()),exp_desd)#1次
            f3.close()#1次

if __name__ == '__main__': #1次
    unittest.main()        #1次
```

f(n)=1+(1+(1+(4)+( (3n^2-6n+3)+3)+( (3n^2)+3) ) )=6n^2-6n+16   ;   T(n)=O(n^2)

f(n)=n+(n+(n+1)+1+1 ) =3n+3                                                             ;   S(n)=O(n)