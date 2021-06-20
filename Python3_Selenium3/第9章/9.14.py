'''
��ҳ����Ϊ�˲��Ի�Ʊ��ѯ��ҳ��Ԫ�صĹ��ܡ�
'''
from selenium.webdriver.common.action_chains import ActionChains
from functions import date_n,id,css,xpath,js,return_driver,open_base_site
#from selenium import webdriver
import time

#���±���Ϊ����������Ʊ�ĳ���վ�͵���վ��
driver =return_driver()
open_base_site("https://trains.ctrip.com/TrainBooking/SearchTrain.aspx")
from_station = "�Ϻ�"
to_station = "����"

#����Ϊtomorrow����
tomorrow = date_n(1)

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

#��ҳ����תʱ����Ǽ�һЩʱ��ȴ��Ĳ��裬�����һЩԪ�ض�λ���쳣���֡�
time.sleep(2)

#�ڳ���K1805���ε�Ӳ��������Ԥ����ť����Ԥ����Ʊ,
#�˴�Ϊ�˴���Ľ�׳����Ҫ�õ�xpath��ģ���ѯ����ǿ���Դ���
xpath("//div[starts-with(@id,'tbody-01-K1805')]/div[1]/div[6]/div[1]/a").click()

#���²�����Ϊ��ʵ�ֲ��õ�¼��Я��ϵͳ��ʵ�ֶ�Ʊ��Ŀ�ġ�
time.sleep(5)

#���� �����������󻯵Ĳ�����Ϊ�˽���ű�ż�����ȶ�������
driver.maximize_window()
id("btn_nologin").click()
time.sleep(3)

#���²������ڶ�����Ϣҳ������˿�������Ϣ
css("#pasglistdiv > div > ul > li:nth-child(2) > input").send_keys("С��")

�������÷����������£�
from datetime import datetime,date,timedelta
from selenium import webdriver

#����Ϊdriver���úʹ�Я�̻�Ʊ��վ
driver =webdriver.Chrome()
'''
����return_driver()��Ϊ�˷���driver����
'''
def return_driver():
    return driver
'''
����open_base_site(url)��Ϊ�˴�Я�̻�Ʊ��ҳ��
'''
def open_base_site(url):
    #driver.get("https://trains.ctrip.com/TrainBooking/SearchTrain.aspx")
    driver.get(url)
'''
����date_n(n) Ϊ����n��������
'''
def date_n(n):
    return str((date.today() + timedelta(days = +int(n))).strftime("%Y-%m-%d"))
'''
����idΪ���ذ���id��������λԪ�ص����
'''
def id(element):
    return driver.find_element_by_id(element)

'''
����css�Ƿ��ذ���css selector��ʽ����λԪ�ص����
'''
def css(element):
    return driver.find_element_by_css_selector(element)
'''
����xpath�Ƿ��ذ���xpath��ʽ����λԪ�ص����
'''
def xpath(element):
    return driver.find_element_by_xpath(element)

'''
����jsΪͨ��selenium��ִ��javascript���
'''
def js(element):
    driver.execute_script("document.getElementById(" + "'" + element + "'" + ").removeAttribute('readonly')")
