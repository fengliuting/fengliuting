import unittest

from 关键字驱动.baseLogic.base import WebDemo


class Test01(unittest.TestCase):
    # 前置条件：class级别
    @classmethod
    def setUpClass(cls) -> None:
        cls.t=WebDemo('Chrome')
        cls.t.open('http://www.baidu.com')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.t.quit()

    # 前置条件:method级别
    def setUp(self) -> None:
        pass

    # 后置条件
    def tearDown(self) -> None:
        self.t.clean('id','kw')
    def test_01(self):
        self.t.input('id','kw','小泽玛利亚')
        self.t.click('id','su')
        self.t.wait(3)

    def test_02(self):
        self.t.input('id','kw','三上优亚')
        self.t.click('id','su')
        self.t.wait(3)

if __name__ == '__main__':
    unittest.main()