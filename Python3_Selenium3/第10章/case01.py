import unittest
import time
class Test1(unittest.TestCase):
    def setUp(self):
        print("��ʼִ�нű�01")
    def tearDown(self):
        time.sleep(3)
        print("�ű�01ִ�н�����")
    def test_01(self):
        print("ִ�е�һ��������")
    def test_02(self):
        print("ִ�еڶ����ű���")
    def test_03(self):
        print("ִ�е������ű���")
if __name__ == "__main__":
    unittest.main()
