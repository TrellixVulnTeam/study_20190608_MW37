#coding=utf-8
from behave import *
from features.com.page.loginPage import loginPage

#����re��ʾ��step�ж���������ʽ��Ҫʹ��������ʽ
use_step_matcher('re')

#�����ʾ��ʼץȡ������ʽ��ƥ��ֵ���˴���Ϊ��ץȡ�ڳ����ļ�example.feature�е�urlֵ��
#ץȡ��֮��ֵ��url��Ȼ���������Ĳ���
@when('I open the login website "([^"]*)"')
def step_reg(context,url):
    loginPage(context).get_url(url)
@Then('I input username "([^"]*)"')
def step_r(context,code):
    loginPage(context).login(code)
