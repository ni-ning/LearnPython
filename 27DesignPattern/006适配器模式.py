# -*- coding:utf-8 -*-
'''
将一个类的接口转换成客户希望的另一个接口
适配器模式使得原本由于接口不兼容而不能一起工作的那些类可以一起工作
实现方式：
- 类适配器：使用多继承
- 对象适配器：使用组合
'''

from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        raise NotImplementedError


class AliPay(Payment):
    def pay(self, money):
        print('阿里支付%d' % money)


class WechatPay(Payment):
    def pay(self, money):
        print('微信支付%d' % money)


# 不接口规范, cost --> pay
class BankPay(object):
    def cost(self, money):
        print('银行卡支付%d' % money)


# 类适配器
class NewBankPay(Payment, BankPay):
    def pay(self, money):
        self.cost(money)


p = NewBankPay()
p.pay(1000)


# 对象适配器，通过组合完成
class PaymentAdapter(Payment):
    def __init__(self, payment):
        self.payment = payment

    def pay(self, money):
        self.payment.cost(money)


p1 = PaymentAdapter(BankPay())
p1.pay(2000)

'''
适用场景：
想使用一个已经存在的类，而它的接口不符合你的要求
'''