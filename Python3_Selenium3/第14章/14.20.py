#coding=utf-8
import threading
from time import sleep

def dispaly_name(user_name):
    sleep(2)
    print('�û���Ϊ�� %s' % user_name)

class MyThread(object):
    def __init__(self,func,args,name=""):
        self.func = func
        self.args = args
        self.name = name
    def __call__(self):
        self.func(self.args)

if __name__ == "__main__":
    t1 = threading.Thread(target=MyThread(func=dispaly_name,args=("С��",)))
    t2 = threading.Thread(target=MyThread(func=dispaly_name,args=("С��",)))

    t1.start()
    t6.start()

    t1.join(1)
    t6.join(2)
    print('�̲߳���������')
