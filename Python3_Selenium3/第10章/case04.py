import unittest
import time
class Test1(unittest.TestCase):
    def setUp(self):
        print("��ʼִ�нű�04")
    def tearDown(self):
        time.sleep(3)
        print("�ű�04ִ�н�����")
    def test_10(self):
        print("ִ�е�10��������")
    def test_11(self):
        print("ִ�е�11���ű���")
    def test_12(self):
        print("ִ�е�12���ű���")
if __name__ == "__main__":
    unittest.main()
