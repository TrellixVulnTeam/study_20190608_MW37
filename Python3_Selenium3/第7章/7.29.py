#coding=utf-8
dict_1 = {'Name': 'Jack','Age':18,'Score':100}
print("�����ֵ�Ԫ��֮ǰ����������ӡ�ֵ�Ԫ�����£�")
for (key,value) in dict_1.items():
    print(key + ":" + str(value))

del dict_1
print("�����ֵ�Ԫ��֮�󣬱�������ӡ�ֵ�Ԫ�����£�")
print(dict_1)
for (key,value) in dict_1.items():
    print(key + ":" + str(value))
