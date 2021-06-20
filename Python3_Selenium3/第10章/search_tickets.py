'''
��ҳ����Ϊ�˲��Ի�Ʊ��ѯ��ҳ��Ԫ�صĹ��ܡ�
'''
from selenium.webdriver.common.action_chains import ActionChains
from functions import date_n,id,css,xpath,js,return_driver,open_base_site
#from selenium import webdriver
import time

'''
�������� search_tickets
������
 from_station: ����վ
 to_station: ����վ
 n�� ��һ�����֣���1��ʾѡ������ĳ�Ʊ��2��ʾѡ�����ĳ�Ʊ��
'''

def search_tickets(from_station,to_station,n):
    driver =return_driver()
    open_base_site("https://trains.ctrip.com/TrainBooking/SearchTrain.aspx")
    #from_station = "�Ϻ�"
    from_station = from_station
    #to_station = "����"
    to_station = to_station

    #����Ϊtomorrow����
    tomorrow = date_n(n)

    #����Ϊ��λ�������к͵�����е�ҳ��Ԫ�أ�����������ֵΪ���϶���ֵ��
    id("notice01").send_keys(from_station)
    id("notice08").send_keys(to_station)

    #���´���Ϊ�Ƴ�����ʱ���'readonly'���ԡ�
    js("dateObj")
    time.sleep(2)
    #�������ʱ���Ĭ�����ݡ�
    id("dateObj").clear()
    time.sleep(2)
    #����Ϊ���������������ڡ�
    id("dateObj").send_keys(tomorrow)

    #���²�����Ϊ�˽�����ڿؼ����������������ں��޷���ʧ�����⣬�Ӷ�Ӱ����ԵĽ��С�
    #ԭ����Ϊ�������������ҳ��հ״���

    ActionChains(driver).move_by_offset(0,0).click().perform()

    #����Ϊ�������������ť
    id("searchbtn").click()
���Դ����ļ�test_booking_tickets.py���¡�
import time
from functions import date_n,id,css,xpath,js,return_driver,open_base_site
from functions import read_excel
from functions import log
from search_tickets import search_tickets

#���´���Ϊ������Ʊ�б�
#search_tickets("�Ϻ�","����",1)
log("Read Excel Files to get test data.")
dic1 = read_excel("testdata.xlsx",0)
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
