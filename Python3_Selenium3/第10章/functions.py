from datetime import datetime,date,timedelta
from selenium import webdriver
import xlrd
import logging

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

#��������ӵĺ��������ڴ���ͻ�ȡExcel�ļ��еĲ������ݡ�
def read_excel(filename,index):
    xls = xlrd.open_workbook(filename)
    sheet = xls.sheet_by_index(index)
    #print(sheet.nrows)
    #print(sheet.ncols)
    dic={}
    for j in range(sheet.ncols):

        data=[]
        for i in range(sheet.nrows):
          data.append(sheet.row_values(i)[j])
        dic[j]=data
    return dic

def log(str):
    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='log-selenium.log',
                    filemode='a')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    logging.info(str)
