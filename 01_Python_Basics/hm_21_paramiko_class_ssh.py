#!/usr/bin/env python3
# coding=utf-8
# 封装ssh类, 用paramiko模块来实现ssh操作
# 把登录的用户名密码信息放在一个配置文件里,作为参数来读取,本例子是SSH登录家里的虚拟机,
# 本例子可以运行在windows和linux平台
# https://www.cnblogs.com/zhangxinqi/p/8372774.html   参考这个链接
import configparser
import paramiko


class ParamikoClient(object):
    def __init__(self, ini_file):    # 只需要从外界传进来一个参数
        self.config = configparser.ConfigParser()
        self.config.read(ini_file)
        self.host = self.config.get('ssh', 'host')
        self.port = self.config.get('ssh', 'port')
        self.user = self.config.get('ssh', 'user')
        self.pwd = self.config.get('ssh', 'pwd')
        self.timeout = self.config.get('ssh', 'timeout')
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=self.host,
                            port=self.port,
                            username=self.user,
                            password=self.pwd,
                            timeout=float(self.timeout))
        self.log_file = "ssh_record.log"  # 存储日志
        
    def run_ssh(self, cmd_command):
        # 执行命令，输出结果在stdout中，如果是错误则放在stderr中
        stdin, stdout, stderr = self.client.exec_command(cmd_command)
        result = stdout.read() + stderr.read()      # read方法读取输出结果
        with open(self.log_file, 'a+') as f:
            print(str(result, 'utf-8'))      # 将二进制机器码码流转化为字符串
            f.write('run cmd: %s\n' % cmd_command)
            f.write(str(result, 'utf-8'))

    def sftp_put(self):
        with self.client.open_sftp() as sftp:
            sftp.put('test.log', 'test.log')
            sftp.chmod('test.log', 755)

    def sftp_get(self):
        with self.client.open_sftp() as sftp:
            sftp.get('test.log', 'test.log')

    def close(self):
        self.client.close()


if __name__ == '__main__':
    client_cmd = ParamikoClient('config.ini')   # 初始化一个类的对象实例
    while True:    # 实际当中可以根据需要是否要用循环
        cmd_input = input('>>>:')      # 判断输入，如果是空或者quit
        if cmd_input == 'quit':
            client_cmd.close()
            break          # ,不再执行命令，跳出循环体
        if cmd_input == ' ':
            pass
        client_cmd.run_ssh(cmd_input)     # 其它输入的处理

