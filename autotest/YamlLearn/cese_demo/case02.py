import ddt
import unittest


@ddt.ddt
class CaseDemo(unittest.TestCase):
    @ddt.data((1,2,3),(4,5,6))
    @ddt.unpack   #分解数据
    def test_01(self, a,b,c):
        print(a,b,c)


if __name__ == '__main__':
    unittest.main()