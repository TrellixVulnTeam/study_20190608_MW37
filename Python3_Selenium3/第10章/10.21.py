import yaml
#����Ϊ��yaml��ʽ����ת��ΪPython list �������͵����ݡ�
file_2 = open('config6.yml')
yml = yaml.load(file_2,Loader=yaml.FullLoader)
print(yml)
print(type(yml))
#����Ϊ��yaml��ʽ������ת��Ϊ�������͵����ݣ����а���list���ֵ��������͡�
file_3 = open('config6.yml')
yml_3 = yaml.load(file_3,Loader=yaml.FullLoader)
print(yml_3)
print(type(yml_3))	
