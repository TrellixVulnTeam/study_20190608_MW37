#coding=utf-8
class animal:

	  #����������ԣ��������䣩
age =10 
#Python�ĳ�ʼ������
    def __init__(self,name): 
        self.name=name
     #��ĳ�Ա����
    def eat(self): 
        print("have something")
        print(self.name)

#��������bird�̳и���animal
class bird(animal):
    #��������ĳ�ʼ������
def __init__(self,name,color): 
    #���ﶨ��ķ��������������û�ж���name������ô�ͼ̳и����name���ԣ���������ж�����name���ԣ���ô��ʹ�����ඨ������ԡ�
        super(bird,self).__init__(name) 
        #��������color
        self.color=color
    #���巽��fly
    def fly(self):
        print(self.name)
        print(self.color)

#��ʼִ�У��е�����java��main�������൱�ڳ��������ڣ�����ֱ����������ִ�еȡ�
if __name__=='__main__':
a = animal("xiaoli")
a.eat()
    #ʵ��������Ĳ�����
    b =bird("xiaoniao","red") 
    b.fly()
b.eat()
#��ӡ����b������ֵ�����ֵ����ʽ��
    print(b.__dict__)
