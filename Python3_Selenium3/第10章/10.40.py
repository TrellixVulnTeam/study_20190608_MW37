# encoding = utf-8
import unittest
import HTMLTestRunner
from selenium import webdriver
import time
import math

# ����һ��������
class SuiteTest1(unittest.TestCase):  # ����һ��������
    def setUp(self):
        # ����chrome�����
        self.driver = webdriver.Chrome()

    def testBaidu(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id("kw").clear()
        self.driver.find_element_by_id("kw").send_keys(u"python")
        self.driver.find_element_by_id("su").click()
        time.sleep(5)
        assert u"python" in self.driver.page_source, "ҳ���в�����Ҫ�����Ĺؼ��֣�"

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(SuiteTest1("testBaidu"))
#��Ϊ���������ɵı���html�ļ���ַ��
    file_name = "D:\\test1.html" 
    # fp = file(file_name,'wb')
    fp = open(file_name, 'wb')
#�˲���Ϊ�����ñ���ҳ���title�ͱ����ܽ��������ݡ�

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test_Report_Portal', description='Report_Description')    runner.run(suite)
    fp.close()
    print("������ɣ�")
