import unittest

'''
 unittest框架应用：
    1.类名继承unittest.TestCase
    2.测试用例：所有的测试用例都是以函数的形式存在。函数的名称必须以test开头
    3.用例加载顺序：0-9，A-Z,a-z;比如：test_add() 和 test_bdd(),先执行用例test_add()
    4.所有的前置后置条件都有等级存在：class级别，method级别
    5.method级别前置后置：与用例关联，每一条用例运行前都会执行一遍前置条件，用例运行后会执行后置条件
    6.class级别前置后置：
        1）必须定义装饰圈@classmethod
        2）前置是在所有内容执行前执行一次，后置是在所有内容执行后执行一次
    7.cls对象只在class级别前置和后置中定义，其他的调用则还是用self进行调用
    8.修改cls对象的值在全局生效：需要通过（类型名.对象  如：Test.tittle=XXX)来赋值才能生效，如果是通过（self.对象=XXX)累操作，只能在
        当前函数中生效
'''

class Test(unittest.TestCase):
    # 前置条件：class级别
    @classmethod
    def setUpClass(cls) -> None:
        print("这是class前置条件")

    @classmethod
    def tearDownClass(cls) -> None:
        print("这是class后置条件")
    # 前置条件:method级别
    def setUp(self) -> None:
        print("这是前置条件")
    # 后置条件
    def tearDown(self) -> None:
        print("这是后置条件")
    # 测试用例 所有的测试用例都是以函数的形式存在。函数的名称必须以test开头
    def test_demo01(self):
        print("这是用例1")
    def test_demo02(self):
        print("这是用例2")

if __name__ == '__main__':
    unittest.main()