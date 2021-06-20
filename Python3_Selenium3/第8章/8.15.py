from datetime import datetime,date,timedelta
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
#����Ϊ���庯�����֣���Ŀ����Ϊ�˷��ؽ����ĵ�n������ڣ���ʽΪ��2019-04-06��
def date_n(n):
    return str((date.today() + timedelta(days = +int(n))).strftime("%Y-%m-%d"))
#���±���Ϊ����������Ʊ�ĳ���վ�͵���վ��
from_station = "�Ϻ�"
to_station = "����"
#����Ϊtomorrow����
tomorrow = date_n(1)
driver = webdriver.Chrome()
driver.get("https://trains.ctrip.com/TrainBooking/SearchTrain.aspx")
#����Ϊ��λ�������к͵�����е�ҳ��Ԫ�أ�����������ֵΪ���϶���ֵ��
driver.find_element_by_id("notice01").send_keys(from_station)
driver.find_element_by_id("notice08").send_keys(to_station)
#���´���Ϊ�Ƴ�����ʱ���'readonly'���ԡ�
driver.execute_script("document.getElementById('dateObj').removeAttribute('readonly')")
time.sleep(2)
#�������ʱ���Ĭ�����ݡ�
driver.find_element_by_id("dateObj").clear()
time.sleep(2)
#����Ϊ���������������ڡ�
driver.find_element_by_id("dateObj").send_keys(tomorrow)
#���²�����Ϊ�˽�����ڿؼ����������������ں��޷���ʧ�����⣬�Ӷ�Ӱ����ԵĽ��С�
#ԭ����Ϊ�������������ҳ��հ״���
ActionChains(driver).move_by_offset(0,0).click().perform()
#����Ϊ�������������ť
driver.find_element_by_id("searchbtn").click()
#��ҳ����תʱ����Ǽ�һЩʱ��ȴ��Ĳ��裬�����һЩԪ�ض�λ���쳣���֡�
time.sleep(2)
#�ڳ���K1805���ε�Ӳ��������Ԥ����ť����Ԥ����Ʊ
driver.find_element_by_css_selector("#tbody-01-K18050 > div.railway_list > div.w6 > div:nth-child(1) > a").click()
#���²�����Ϊ��ʵ�ֲ��õ�¼��Я��ϵͳ��ʵ�ֶ�Ʊ��Ŀ�ġ�
driver.find_element_by_id("btn_nologin").click()
