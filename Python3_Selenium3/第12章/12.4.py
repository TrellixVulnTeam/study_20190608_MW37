
###
###������Ƶ�ѳ��棬ѧϰ��������ϵ����qq:2574674466###
###
#coding=utf-8
from behave import given, when, then, step

@given('we have behave installed')
def step_impl(context):
    pass
#ע�⣬���µ�ʵ�ֺ�����У������н�>1�ĳ�>10
@when('we implement {number:d} tests')
def step_impl(context, number):
    assert number > 10 or number == 0
    context.tests_count = number
@then('behave will test them for us!')
def step_impl(context):
    assert context.failed is False
    assert context.tests_count >= 0
