
###
###������Ƶ�ѳ��棬ѧϰ��������ϵ����qq:2574674466###
###
#coding=utf-8
'''
ʵ�ֻ�Ʊ��ѯ��ҳ��Ԫ�صĹ��ܡ�
'''
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://trains.ctrip.com/TrainBooking/SearchTrain.aspx")
#���±���Ϊ����������Ʊ�ĳ���վ�͵���վ��
from_station = "�Ϻ�"
to_station = "����"
#����Ϊ��λ�������к͵�����е�ҳ��Ԫ��
driver.find_element_by_id("notice01").send_keys(from_station)
driver.find_element_by_id("notice08").send_keys(to_station)
driver.find_element_by_id("dateObj").send_keys("2019-04-12")
#����Ϊ��λ����������ť
driver.find_element_by_id("searchbtn").click()
