import unittest
import HTMLTestRunner
import os

class RunTools(object):
    def __init__(self, case_path, pattern):
        self.case_path = case_path
        self.pattern = pattern

    def choose_all_cases(self):
        discover_all_cases = unittest.defaultTestLoader.discover(self.case_path, self.pattern)
        return discover_all_cases


if __name__ == '__main__':
    ####
    case_dir = os.path.dirname(__file__)
    run = RunTools(case_dir, 'web*.py')
    suite = run.choose_all_cases()
    #####
    file_name = os.path.dirname(__file__) + '/report.html'
    with open(file_name, 'wb+') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='report', description='web api test')
        runner.run(suite)