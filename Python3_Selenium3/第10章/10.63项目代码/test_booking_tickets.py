import time
import unittest
import HTMLTestRunner
from functions import date_n,id,css,xpath,js,return_driver,open_base_site
from functions import read_excel
from functions import log
from search_tickets import search_tickets

#���´���Ϊ������Ʊ�б�
#search_tickets("�Ϻ�","����",1)
class booking_tickets(unittest.TestCase):
    def setUp(self):
        self.driver = return_driver()

    def test_ctrip_tickets(self):
        log("Read Excel Files to get test data.")
        dic1 = read_excel("testdata.xlsx",0)
        print(dic1[0][0],dic1[0][1])

        log("Begin to search tickets")
        search_tickets(dic1[0][0],dic1[0][1],1)
        log("End to search tickets")
        log("Begin to get driver object.")
        driver = return_driver()

        #��ҳ����תʱ����Ǽ�һЩʱ��ȴ��Ĳ��裬�����һЩԪ�ض�λ���쳣���֡�
        time.sleep(2)

        #�ڳ���K1805���ε�Ӳ��������Ԥ����ť����Ԥ����Ʊ,
        #�˴�Ϊ�˴���Ľ�׳����Ҫ�õ�xpath��ģ���ѯ����ǿ���Դ���
        log("Click book button :)")
        xpath("//div[starts-with(@id,'tbody-01-K1805')]/div[1]/div[6]/div[1]/a").click()

        #���²�����Ϊ��ʵ�ֲ��õ�¼��Я��ϵͳ��ʵ�ֶ�Ʊ��Ŀ�ġ�
        time.sleep(5)
        #���� �����������󻯵Ĳ�����Ϊ�˽���ű�ż�����ȶ�������
        driver.maximize_window()
        id("btn_nologin").click()
        time.sleep(3)

        #���²������ڶ�����Ϣҳ������˿�������Ϣ
        #css("#pasglistdiv > div > ul > li:nth-child(2) > input").send_keys("С��")
        log("input order information")
        css("#pasglistdiv > div > ul > li:nth-child(2) > input").send_keys(dic1[0][2])
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(booking_tickets("test_ctrip_tickets"))
    file_name = "D:\\report_ctrip_tickets.html" #��Ϊ���������ɵı���html�ļ���ַ��
    # fp = file(file_name,'wb')
    fp = open(file_name, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test_Report_Portal', description='Report_Description') #�˲���Ϊ�����ñ���ҳ���title�ͱ����ܽ��������ݡ�
    runner.run(suite)
    fp.close()
