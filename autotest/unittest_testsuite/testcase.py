import unittest

class Test(unittest.TestCase):
    # 前置条件：class级别
    # @classmethod
    # def setUpClass(cls) -> None:
    #     print("这是class前置条件")
    #
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print("这是class后置条件")
    # # 前置条件:method级别
    # def setUp(self) -> None:
    #     print("这是前置条件")
    # # 后置条件
    # def tearDown(self) -> None:
    #     print("这是后置条件")
    # 测试用例 所有的测试用例都是以函数的形式存在。函数的名称必须以test开头
    def test_demo01(self):
        print("这是用例1")
    def test_demo02(self):
        print("这是用例2")

    def test_demo03(self):
        print("这是用例3")
if __name__ == '__main__':
    unittest.main()