#coding=utf-8
list_1 = [3,6,9,"selenium","8.9093",["a","B","C","abc"]]
print("����Ϊֱ�Ӵ�ӡ����list�б�")
print(list_1)
print("\n") #���в���
print("����Ϊ��������б��Ԫ�أ�����ӡ��")
for l in list_1: #forѭ���������е��б�Ԫ�أ�����ӡ
    print(l)



#coding=utf-8
list_1 = [3,6,9,"selenium","8.9093",["a","B","C","abc"]]
print("append����б�Ԫ��֮ǰ�������б�Ԫ�أ�����ӡ")
for l in list_1: #forѭ���������е��б�Ԫ�أ�����ӡ
    print(l)
list_1.append("a_append")
print("\n") #���в���
print("append����б�Ԫ��֮�󣬱����б�Ԫ�أ�����ӡ")
for l in list_1: #forѭ���������е��б�Ԫ�أ�����ӡ
    print(l)


#coding=utf-8
list_1 = [3,6,9,"selenium","8.9093",["a","B","C","abc"]]
print("append����б�Ԫ��֮ǰ�������б�Ԫ�أ�����ӡ")
for l in list_1: #forѭ���������е��б�Ԫ�أ�����ӡ
    print(l)
list_1.extend(['e','f','g'])
print("\n") #���в���
print("append����б�Ԫ��֮�󣬱����б�Ԫ�أ�����ӡ")
for l in list_1: #forѭ���������е��б�Ԫ�أ�����ӡ
    print(l)

##### 5.10
#coding=utf-8
list_1 = [3,6,9,"selenium","8.9093",["a","B","C","abc"]]
print("append����б�Ԫ��֮ǰ�������б�Ԫ�أ�����ӡ")
for l in list_1: #forѭ���������е��б�Ԫ�أ�����ӡ
    print(l)
list_1.insert(0,"0") #ָ���б�ĵ�1��0+1����λ�������Ԫ��"0"
print("\n") #���в���
print("append����б�Ԫ��֮�󣬱����б�Ԫ�أ�����ӡ")
for l in list_1: #forѭ���������е��б�Ԫ�أ�����ӡ
    print(l)

####5.11
#coding=utf-8
list_1 = [3,6,9,"selenium","8.9093",["a","B","C","abc"]]
print("ִ��ɾ���б�Ԫ��֮ǰ�������б�Ԫ�أ�����ӡ")
for l in list_1: #forѭ���������е��б�Ԫ�أ�����ӡ
    print(l)
list_1.remove(3) #ɾ�� '3'����б�Ԫ��
print("\n") #���в���
print("ִ��ɾ���б�Ԫ��֮�󣬱����б�Ԫ�أ�����ӡ")
for l in list_1: #forѭ���������е��б�Ԫ�أ�����ӡ
    print(l)



#5.12
list_1 = [3,6,9,"selenium","8.9093",["a","B","C","abc"]]
print("ִ��ɾ���б�Ԫ��֮ǰ�������б�Ԫ�أ�����ӡ")
for l in list_1: #forѭ���������е��б�Ԫ�أ�����ӡ
    print(l)
del list_1[1] #ɾ�� λ�����Ϊ1��Ԫ�أ�Ҳ�����б��е�2��Ԫ�ء�
print("\n") #���в���
print("ִ��ɾ���б�Ԫ��֮�󣬱����б�Ԫ�أ�����ӡ")
for l in list_1: #forѭ���������е��б�Ԫ�أ�����ӡ
    print(l)

#5.13
list_1 = [3,6,9,"selenium","8.9093","-9"]
print("ִ��ɾ���б�Ԫ��֮ǰ�������б�Ԫ�أ�����ӡ")
for l in list_1: #forѭ���������е��б�Ԫ�أ�����ӡ
    print(l)
pop_res = list_1.pop()
print("\n")
print("pop()�������ص�Ԫ�أ�"+pop_res)
print("\n") #���в���
print("ִ��ɾ���б�Ԫ��֮�󣬱����б�Ԫ�أ�����ӡ")
for l in list_1: #forѭ���������е��б�Ԫ�أ�����ӡ
    print(l)


#5.14
list_1 = [3,6,9,"selenium","8.9093","-9"]
print("�б��Ƭ֮ǰ�������б�Ԫ�أ�����ӡ")
for l in list_1: #forѭ���������е��б�Ԫ�أ�����ӡ
    print(l)

print("\n") #���в���
temp = list_1[3] #���ص���һ���ַ��������б��еĵ�4��Ԫ�ء�
print(temp)

temp = list_1[2:4] #������Ƭ�����ص���һ���µ��б�temp,�б�Ԫ��Ϊ���б�ĵ�3��4��Ԫ����ɡ�
print(temp)
print("�б��Ƭ֮�󣬱����б�Ԫ�أ�����ӡ")
for l in list_1: #forѭ���������е��б�Ԫ�أ�����ӡ
    print(l)

#5.15
list_1 = [3,6,9,"selenium","8.9093","-9"]
list_2 = [1,4,7,"python","9.9999","-10"]
print("�����б�1������ӡ")
for l in list_1: #forѭ���������е��б�Ԫ�أ�����ӡ
    print(l)

print("�����б�2������ӡ")
for l in list_2: #forѭ���������е��б�Ԫ�أ�����ӡ
    print(l)

list_3 = list_1 + list_2
print("����ƴ�Ӻ���б�����ӡ")
for l in list_3:
    print(l)


#5.16
list_1 = [3,6,9,"selenium","8.9093","-9"]
print("�����б�1������ӡ")
for l in list_1: #forѭ���������е��б�Ԫ�أ�����ӡ
    print(l)

list_3 = list_1*3
print("����ƴ�Ӻ���б�����ӡ")
for l in list_3:
    print(l)


#5.17
list_1 = [1,2,3,4,5]
list_2 = [6,7,8,9,10]
print("�����б�1������ӡ")
for l in list_1: #forѭ���������е��б�Ԫ�أ�����ӡ
    print(l)

print("�����б�2������ӡ")
for l in list_2: #forѭ���������е��б�Ԫ�أ�����ӡ
    print(l)

print(list_1 > list_2)
print(list_1 < list_2)




