import sys
sys.path.append('..')
from publishs import mod
import unittest,num_threading

class TestCase(unittest.TestCase):
    def test_pos_num(self):
        self.assertEqual(type(num_threading.file_size),int)
    def test_file_reader(self):
        lis = num_threading.list

        with open('original_file','r') as f1:
            lis1 = num_threading.list
            exp_org = int(''.join(str(i) for i in lis1))
            self.assertEqual(int(f1.read()),exp_org)
            f1.close()

        with open('ascend_file','r') as  f2:
            mod.bublle_sort(lis)
            exp_asd=int(''.join(str(i) for i in lis))
            self.assertEqual(int(f2.read()), exp_asd)
            f2.close()

        with open('descend_file','r') as  f3:
            mod.insertion_sort(lis)
            exp_desd=int(''.join(str(i) for i in lis))
            self.assertEqual(int(f3.read()),exp_desd)
            f3.close()

if __name__ == '__main__':
    unittest.main()


