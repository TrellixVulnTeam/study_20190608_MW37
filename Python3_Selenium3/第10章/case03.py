import unittest
import time
class Test1(unittest.TestCase):
    def setUp(self):
        print("��ʼִ�нű�03")
    def tearDown(self):
        time.sleep(3)
        print("�ű�03ִ�н�����")
    def test_07(self):
        print("ִ�е�7��������")
    def test_08(self):
        print("ִ�е�8���ű���")
    def test_09(self):
        print("ִ�е�9���ű���")
if __name__ == "__main__":
    unittest.main()
