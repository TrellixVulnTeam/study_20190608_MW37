#coding=utf-8
from selenium.webdriver.common.by import By
class Base:
    def __init__(self,driver):
        self.driver = driver

     #*loc ����������ָ������ǲ������������֪ʶ����ǰ���½��Ѿ��ᵽ��
     #��˼��findele�������Դ���1��������Ҳ���Դ���2�������ȵȡ�
    def findele(self,*loc):
        return  self.driver.find_element(*loc)

    def get_url(self,url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title
