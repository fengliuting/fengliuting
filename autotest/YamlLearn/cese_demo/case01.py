import ddt
import unittest


@ddt.ddt
class CaseDemo(unittest.TestCase):
    @ddt.file_data('../data/data04.yaml')
    def test_01(self,**kwargs):
        print(kwargs['姓名'])
        

if __name__ == '__main__':
    unittest.main()