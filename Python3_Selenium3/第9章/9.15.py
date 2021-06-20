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
