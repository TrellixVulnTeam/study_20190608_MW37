#coding=utf-8
from behave import given, when, then, step
@given('we have behave installed')
def step_impl(context):
    pass
# ��������number����ת������������
#���º�����Ϊ�˻�ȡ�ڳ����ļ������õ����� 5��Ȼ�������жϵȲ�����
@when('we implement {number:d} tests')
def step_impl(context, number):
    assert number > 1 or number == 0
    context.tests_count = number
@then('behave will test them for us!')
def step_impl(context):
    assert context.failed is False
    assert context.tests_count >= 0
