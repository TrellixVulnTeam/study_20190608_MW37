#encoding = utf-8
import unittest
from selenium import webdriver
import time
#driver = webdriver.chrome()
class add(unittest.TestCase): #����һ��������
    def setUp(self):
        #����chrome�����
        self.driver = webdriver.Chrome()

    def testBaidu(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id("kw").clear()
        self.driver.find_element_by_id("kw").send_keys(u"python")
        self.driver.find_element_by_id("su").click()
        time.sleep(5)
        assert u"python" in self.driver.page_source,"ҳ���в�����Ҫ�����Ĺؼ��֣�"

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
