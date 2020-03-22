import os
import threading
import random
import sys
sys.path.append('..')
from publishs import mod


#生成随机数组文件
def generate_orig(data_size,list):
    while data_size < file_size:
        list.append(random.randint(1, 9))
        mod.file_accessor('original_file', list)
        data_size = os.path.getsize('original_file')
    print(os.path.getsize('original_file'))
#正序
def ascending_file():
    list1=list.copy()
    mod.bublle_sort(list1)
    mod.file_accessor('ascend_file',list1)
    data_size = os.path.getsize('ascend_file')
    print(os.path.getsize('ascend_file'))
    print('thread1 pass')
#逆序
def descending_file():
    list2=list.copy()
    mod.insertion_sort(list2)
    mod.file_accessor('descend_file',list2)
    data_size = os.path.getsize('descend_file')
    print(os.path.getsize('descend_file'))
    print('thread2 pass')
#多线程
def main():
    thread1=threading.Thread(target=ascending_file(),name='T1')
    thread2=threading.Thread(target=descending_file(),name='T2')
    thread1.start()
    thread2.start()
# 执行
input_size=input('请输入文件大小：')
list = []
data_size = 0
if mod.positive_num(input_size):
    file_size = int(input_size)
    generate_orig(data_size,list)
    main()