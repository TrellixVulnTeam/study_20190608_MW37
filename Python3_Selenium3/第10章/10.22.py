import os #�����ļ�����Ҫ����'os'ģ��
print(os.getcwd()) # ��ӡ����ǰִ�нű�����Ŀ¼
print(os.path.exists('/PycharmProjects/Sstone/tt.png')) #�����ǰ·�������򷵻�"True"������������򷵻�"False"
print(os.path.isfile('/PycharmProjects/Sstone/tt.png')) #�жϵ�ǰ·���Ƿ���һ���ļ�������ǣ��򷵻�"True"
#os.remove('/PycharmProjects/Sstone/tt.png') #ɾ��һ���ļ�
os.removedirs('/PycharmProjects/Sstone/')  #����ɾ���༶Ŀ¼
os.mkdir("test1221") #�ڵ�ǰĿ¼�´���'test1221' �����ļ���
os.makedirs('/PycharmProjects/Sstone/1/2/3') #���Դ����༶Ŀ¼
