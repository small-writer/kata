#冒泡 顺序
def bublle_sort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]



#插入 逆序
def insertion_sort(list):
    for i in range(1, len(list)):
        value = list[i]
        for j in range(i - 1, -1, -1):
            if list[j] < value:
                list[j + 1] = list[j]
                list[j] = value


#文件创建和读写
def file_accessor(filename,seq):
    f=open(filename, 'w+')
    f.write(''.join(str(i) for i in seq))
    f.close()


#输入正数
def positive_num(num):
    if num.isdigit() and int(num) > 0:
        return True
    else:
        print('请输入正数')