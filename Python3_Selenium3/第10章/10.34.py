import unittest
class add(unittest.TestCase): #����һ��������
    def setUp(self):
        pass
    def test_01(self):
        self.assertEqual(2,2) # test_01������Ϊ���ж� 2 �� 2�Ƿ���ȣ�Ԥ�ڽ�������
    def test_02(self):
        self.assertEqual('selenium','appium') #test_02������Ϊ���ж�"selnium"�ַ�����"appium"�Ƿ���ȣ�Ԥ�ڽ���ǲ���
    def test_03(self):
        self.assertEqual('se','se')# test_03������Ϊ���ж�"se"�ַ�����"se"�Ƿ�ͬ���ַ�����Ԥ�ڽ�������
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
