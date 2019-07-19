# -*- coding:utf-8 -*-
'''
定义一个用于创建对象的接口(工厂接口)，让子类决定实例化哪一个产品类
'''

from abc import ABCMeta, abstractmethod


# 抽象产品角色(Product)
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


# 具体产品角色(Concrete Product)
class AliPay(Payment):
    def __init__(self, use_huabei=False):
        self.use_huabei = use_huabei

    def pay(self, money):
        if self.use_huabei:
            print('花呗支付%d元' % money)
        else:
            print('支付宝余额支付%d元' % money)


# 具体产品角色(Concrete Product)
class WechatPay(Payment):
    def pay(self, money):
        print('微信支付%d元' % money)


class BankPay(Payment):
    def pay(self, money):
        print('银行卡支付%d元' % money)


# 抽象工厂角色(Creator)
class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        pass


# 具体工厂角色(Concrete Creator)
class AlipayFactory(PaymentFactory):
    def create_payment(self):
        return AliPay()


class WechatFactory(PaymentFactory):
    def create_payment(self):
        return WechatPay()


class BankFactory(PaymentFactory):
    def create_payment(self):
        return BankPay()


ali_factory = AlipayFactory()
p1 = ali_factory.create_payment()
p1.pay(1000)

we_factory = WechatFactory()
p2 = we_factory.create_payment()
p2.pay(2000)


bank_factory = BankFactory()
p3 = bank_factory.create_payment()
p3.pay(3000)

'''
优点:
- 每个具体产品都对应一个具体工厂类，不需要修改原有工厂类代码
- 隐藏了对象创建的实现细节
缺点:
- 每增加一个具体产品类，就必须增加一个相应的具体工厂类
'''