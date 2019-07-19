# -*- coding:utf-8 -*-
'''
不直接向客户端暴露对象创建的实现细节，而是通过一个工厂类来负责创建产品类的实例
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


# 工厂角色(Creator)
class PaymentFactory(object):
    def create_payment(self, method):
        # 隐藏细节
        if method == 'ali':
            # 用户完全不用传递的参数，在工厂里传入
            return AliPay()
        elif method == 'wechat':
            # 或 ali 与 wechat 相同功能 不同格式的参数，如json，xml
            return WechatPay()

        # 新增一种选项，调用时只是选项值增加，而不是参数增加 ********
        elif method == 'huabei':
            return AliPay(use_huabei=True)
        else:
            return None


pf = PaymentFactory()
pf = pf.create_payment('huabei')
pf.pay(1000)

'''
优点：
- 隐藏了对象创建的实现细节
- 客户端不需要修改代码
缺点：
- 违反了单一职责原则，将创建逻辑集中到一个工厂类里
- 当添加新产品时，需要修改工厂类代码，违反了开闭原则
'''