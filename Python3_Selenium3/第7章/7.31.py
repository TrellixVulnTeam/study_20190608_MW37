from selenium import webdriver
import  time
driver = webdriver.Chrome()
driver.get("https://pan.baidu.com/")
	   #����ִ�е��˲�����Ҫ�ֶ�ȥ��¼���ٶ����̡�
time.sleep(20)
cookies=driver.get_cookies()
print(cookies)
