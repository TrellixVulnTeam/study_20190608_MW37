#coding=utf-8
dict_1 = {'Name': 'Jack','Age':18,'Score':100}
print("�����ֵ�Ԫ��֮ǰ����������ӡ�ֵ�Ԫ�����£�")
for (key,value) in dict_1.items():
    print(key + ":" + str(value))

#ɾ���ֵ�Ԫ�� 'Name': 'Jack'
del dict_1['Name']
print("ɾ��һ��Ԫ�غ󣬱�������ӡ�ֵ�Ԫ�����£�")
for (key,value) in dict_1.items():
    print(key + ":" + str(value))
