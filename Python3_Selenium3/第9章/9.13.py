from datetime import datetime,date,timedelta
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
#����Ϊ���庯�����֣���Ŀ����Ϊ�˷��ؽ����ĵ�n������ڣ���ʽΪ��2019-04-06��
def date_n(n):
    return str((date.today() + timedelta(days = +int(n))).strftime("%Y-%m-%d"))

def id(element):
    return driver.find_element_by_id(element)

def css(element):
    return driver.find_element_by_css_selector(element)
def js(element):
    driver.execute_script("document.getElementById(" + "'" + element + "'" + ").removeAttribute('readonly')")
def xpath(element):
    return driver.find_element_by_xpath(element)

#���±���Ϊ����������Ʊ�ĳ���վ�͵���վ��
from_station = "�Ϻ�"
to_station = "����"

#����Ϊtomorrow����
tomorrow = date_n(1)
#����Ϊdriver����
driver = webdriver.Chrome()
driver.get("https://trains.ctrip.com/TrainBooking/SearchTrain.aspx")

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

#�ڳ���K1805���ε�Ӳ��������Ԥ����ť����Ԥ����Ʊ
xpath("//div[starts-with(@id,'tbody-01-K1805')]/div[1]/div[6]/div[1]/a").click()
time.sleep(5)
#������������
driver.maximize_window()
id("btn_nologin").click()
time.sleep(3)
#������Ϣҳ������˿�������Ϣ
css("#pasglistdiv > div > ul > li:nth-child(2) > input").send_keys("С��")
