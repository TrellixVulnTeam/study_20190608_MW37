import ddt
import unittest

@ddt.ddt
class test_se(unittest.TestCase):
    def setUp(self):
        pass

    @ddt.file_data("tt.json") #�ļ� tt.json ���ڵ�ǰ�ļ����ڡ�
    def test_01(self,tt):
        print(tt)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
