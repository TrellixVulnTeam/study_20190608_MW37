import unittest
import time
class Test2(unittest.TestCase):
    def setUp(self):
        print("��ʼִ�нű�02")
    def tearDown(self):
        time.sleep(3)
        print("�ű�02ִ�н�����")
    def test_04(self):
        print("ִ�е�4��������")
    def test_05(self):
        print("ִ�е�5���ű���")
    def test_06(self):
        print("ִ�е�6���ű���")
if __name__ == "__main__":
    unittest.main()
