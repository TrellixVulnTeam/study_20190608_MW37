###
###������Ƶ�ѳ��棬ѧϰ��������ϵ����qq:2574674466###
###

#coding=utf-8
import unittest
class ParaCase(unittest.TestCase):
   #unittest���Ӳ�����
    def __init__(self, methodName='Tests', param=None):
        super(ParaCase, self).__init__(methodName)
        self.driver = param
    def setUp(self):
        self.driver.maximize_window()

@staticmethod
#���·�����Ϊ�˴��������׼������׼������ڱ��̳�������ò���������������Ҫ���еķ�����ֻ��Ҫͨ��param������
    def parametrize(testcase, param=None):
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase(name, param=param))
        return suite
