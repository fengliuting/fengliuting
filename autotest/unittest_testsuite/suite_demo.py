import datetime
import os
import unittest
from unittest_testsuite.testcase import Test
from HTMLTestRunner import HTMLTestRunner

# 创建测试套件
suite= unittest.TestSuite()
# 添加测试用例,第一种方法
# suite.addTest(Test('test_demo01'))
# suite.addTest(Test('test_demo02'))
# 添加测试用例,第二种方法，批量添加
cases = [Test('test_demo01'),Test('test_demo03')]
suite.addTests(cases)
# 添加测试用例,第三种方法,test*.py  当前目录下以test开头的测试类都会执行
# test_dir='./'
# discover= unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test*.py')

# 添加测试用例,第四种方法，指定测试类Test，执行测试类中所有案例
# suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test))

# 添加测试用例,第五种方法loadTestsFromName,文件名.类名
# suite.addTests(unittest.TestLoader().loadTestsFromName('testcase.Test'))

# 基于Runner来运行测试套件
# runner = unittest.TextTestRunner(verbosity=2)
# runner.run(suite)

# 集成测试报告
report_name = '测试报告名称'
report_title = '测试报告标题'
report_desc = '测试报告描述'
# 测试报告保存路径
report_path = './report/'
report_file = report_path + 'report.html'

# 判断文件夹是否存在
if not os.path.exists(report_path):
    os.mkdir(report_path)
else:
    pass

# HTMLTestRunner使用
with open(report_file,'wb') as report:
    # suite.addTests()
    runner = HTMLTestRunner(stream=report,title=report_title,description=report_desc)
    runner.run(suite)

