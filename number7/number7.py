
def is_true(num):
    if num.isdigit() and int(num) > 0:
        return True
    else:
        print('请输入正数')

num=input('n=')
i=1
if is_true(num):
    while i<=int(num):
        if '7' in str(i) or i%7==0:
            print('pass')

        else:
            print(i)
        i+=1