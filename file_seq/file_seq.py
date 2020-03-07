import random
import publishs

def file_accessor(filename,seq):
    f=open(filename, 'w+')
    f.write(','.join(str(i) for i in seq))
    f.close()

seq=list(range(3000))
new_seq=random.sample(seq,random.randint(1,100))

file_accessor('file',new_seq)

publishs.bublle_sort(new_seq)
file_accessor('new_file',new_seq)