#coding=utf-8
#��һ�ִ������ϵķ�ʽ��ֱ�Ӹ�ֵ��
set_1 = {'a','b','c','d','e'}
print("��ӡ����set_1:")
for s in set_1:
    print(s)
#�ڶ��ִ������ϵķ�ʽ����set������
set_2 = set('world')
print("��ӡ����set_2:")
for s in set_2:
    print(s)


#coding=utf-8
#��ʾ��������Ҫ���ж�һ�������Ƿ�������һ�����ϵ��Ӽ���
#������> <���ţ������� issubset()���������ж���
set_1 = set('what')
set_2 = set('whatabout')
set_3 = set('whataboutyou')

print(set_1 < set_2) #Ӧ�÷��� True.
print(set_2 < set_3) #Ӧ�÷��� True.
print(set_3 > set_1) #Ӧ�÷��� True.
print(set_1.issubset(set_2)) #���Ӧ�÷���True.



#coding=utf-8
print("����Ϊ���ϲ����Ĳ�����")
set_1 = set('what')
set_2 = set('whatabout')
set_3 = set('whataboutyou')
#set_a = set_1 | set_2  #��һ�ֲ����ķ���
set_a = set_1.union(set_2)  #�ڶ��ֲ����ķ���
for s in set_a:
    print(s)
print("����Ϊ���Ͻ����Ĳ�����")
set_b = set_1 & set_2 #���ǵ�һ�ֽ����ķ�ʽ
set_b = set_1.intersection(set_2)  #���ǵڶ��ֽ����ķ�ʽ

#��ӡ�������ļ���Ԫ��
for s in set_b:
    print(s)

print("����Ϊ���ϲ�Ĳ�����")
set_c = set_1 - set_2 #��һ�ֲ�ķ�ʽ
set_c = set_1.difference(set_2) #�ڶ��ֲ�ķ�ʽ

#��ӡ����ļ���Ԫ��
for s in set_c:
    print(s)


