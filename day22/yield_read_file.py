# /static/的另一个作用是用来对文件的读取。如果对文件直接采用read（），会导致不可预测的内存占用，
# 一个好的方法是利用一个固定长度的缓存区去不断的读取文件的内容，通过yield方法可以很容易的实现。
import csv


def read_file(fpath):
    block_size = 1024
    with open(fpath, 'rb') as f:
        while True:
            block = f.read(block_size)  # 每次读取1024字节, or you can use f.readline() to read just one line each time
            if block:
                yield block
            else:
                return


def read_csv(fpath):
    with open(fpath) as f:
        f_csv = csv.reader(f)
        headings = next(f_csv)   # there is a heading in this file,so you need to run next() firstly
        for line in f_csv:
            yield line


if __name__ == '__main__':
    res = read_file(r'test_result.log')
    for r in res:
        print(r)

    for t in read_csv('read_csv.csv'):
        print(type(t), t)    # it is a list   <class 'list'> ['1', 'xiaozhan', '20']
# print(type(res))        # <class 'generator'>
# for i in res:
#     print(i)
# print(next(res))  # 调用一次next函数，每次就会读取1024字节
# print(type(next(res)))
# print(next(res))

# 函数执行结果如下：
# b'ICMP-1.1:Passed\nICMP-1.2:Passed\nICMP-1.3:Passed\nICMP-1.5:Passed\nICMP-1.6:Passed\nICMP-2.1:Passed\nICMP-2.2:Passed\nICMP-2.3:Passed\nICMP-2.4:Passed\nICMP-2.5:Passed\nICMP-3.1:Passed\nICMP-3.2:Passed\nICMP-4.1:Passed\nICMP-4.2:Passed\nICMP-4.3:Passed\nICMP-4.4:Passed\nICMP-4.5:Passed\nICMP-5.1:Passed\nICMP-5.2:Passed\nICMP-5.3:Passed\nICMP-7.1:Passed\nICMP-7.2:Passed\nICMP-7.3:Passed\nICMP-7.4:Passed\nICMP-8.1:Passed\nICMP-8.2:Passed\nICMP-8.3:Passed\nICMP-9.1:Passed\nICMP-9.2:Passed\nICMP-9.3:Passed\nICMP-10.1:Passed\nDHCP-SERVER-1.1:Passed\nDHCP-SERVER-1.2:Passed\nDHCP-SERVER-2.1:Passed\nDHCP-SERVER-2.2:Passed\nDHCP-SERVER-2.3:Passed\nDHCP-SERVER-2.4:Passed\nDHCP-SERVER-2.5:Passed\nDHCP-SERVER-2.6:Passed\nDHCP-SERVER-4.1:Passed\nDHCP-SERVER-4.2:Passed\nDHCP-SERVER-4.3:Passed\nDHCP-SERVER-4.4:Passed\nDHCP-SERVER-5.1:Passed\nDHCP-SERVER-5.2:Passed\nDHCP-SERVER-5.3:Passed\nDHCP-SERVER-5.4:Passed\nDHCP-SERVER-5.5:Passed\nDHCP-SERVER-6.1:Passed\nDHCP-SERVER-6.3:Passed\nDHCP-SERVER-6.4:Passed\nDHCP-SERVER-7.1:Passed\nDHCP-SERVER-8.1:Passed\nDHCP-SERVER-8.2:Passe'
# <class 'bytes'>