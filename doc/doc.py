import random

def bubble(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

seq=list(range(3000))
n=random.randint(1,100)
new_seq=random.sample(seq,n)

file1=open('file1','w+')
file1.write(','.join(str(i) for i in new_seq))
file1.close()


bubble(new_seq)
print(new_seq)
file2=open('file2','w+')
file2.write(','.join(str(i) for i in new_seq))
file2.close()


