#coding=utf=8
#���ȸ�һ��������ֵ
a = 10
if a > 10:
    print("���ִ���10")
elif a < 10:
    print("����С��10")
else:
    print("���ֵ���10")




#coding=utf-8
list1 = ["selenium","appium","python","automation"]

#ʹ��forѭ���������б�list1�е����е�Ԫ��
#��һ�ַ�ʽ
for l in list1:
    print(l)

#�ڶ��ַ�ʽ

for index in range(len(list1)):
    print(list1[index])



#coding=utf-8
for i in range(10):
    print(i)
print("***************")
for j in range(2,10,2):
    print(j)
print("***************")
print(type(range(10)))


