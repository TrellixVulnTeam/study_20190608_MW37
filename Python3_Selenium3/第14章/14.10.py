#coding=utf-8
import threading
from time import sleep
#����Ϊ������߳�Ҫʹ�õĺ���
def display_name(user_name):
    sleep(2)
    print('�û���Ϊ�� %s' % user_name)
#����Ϊ���̵߳Ĳ��Դ��룬���̵߳Ĳ���������ʵ��
if __name__ == '__main__':
    t1 = threading.Thread(target=display_name, args=('С��',))
    t2 = threading.Thread(target=display_name, args=('С��',))
    t1.start()
    t6.start()
    t1.join(1)
    t6.join(1)
    print('�̲߳�������!')
