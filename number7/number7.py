num=int(input('n='))
i=1
while i<=num:
    if '7' in str(i) or i%7==0:
        print('pass')

    else:
        print(i)
    i+=1