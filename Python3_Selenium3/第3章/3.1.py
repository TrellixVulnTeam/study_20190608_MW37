###
###������Ƶ�ѳ��棬ѧϰ��������ϵ����qq:2574674466###
###
#����python�Դ���os����ģ��
import os 
#����WebDriverģ��
from selenium import webdriver
#����IE�������WebDriver��������·��
IEDriverServer="C:\\Program Files (x86)\\Internet Explorer\\IEDriverServer.exe"
#���õ�ǰos webdriverΪIE���������������
os.environ["webdriver.ie.driver"] = IEDriverServer
#����IE�����
driver =  webdriver.Ie(IEDriverServer) 
#�򿪰ٶ���ҳ
driver.get('https://www.baidu.com')


#chrome

from selenium import webdriver
#������Ҫ�ƶ���ʵ��Chrome���������·��
ChromeDriverServer="C:\\Users\\xxx\\chromedriver.exe"
driver = webdriver.Chrome(ChromeDriverServer)
driver.get('https://www.baidu.com')

