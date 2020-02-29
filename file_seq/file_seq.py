import random
def num_sort(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

def fileAccessor(filename,seq):
    f=open(filename, 'w+')
    f.write(','.join(str(i) for i in seq))
    f.close()

seq=list(range(3000))
new_seq=random.sample(seq,random.randint(1,100))

fileAccessor('file',new_seq)

num_sort(new_seq)
fileAccessor('new_file',new_seq)