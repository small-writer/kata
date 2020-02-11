num=input('请输入正数：')
i=1
if num.isdigit() and int(num)>0:
    while i<=int(num):
        if '7' in str(i) or i%7==0:
            print('pass')

        else:
            print(i)
        i+=1
else:
    print('请输入正数')