

### 什么是面向对象的程序设计及为什么要有它

面向过程的程序设计的核心是==过程==(流水线式思维)，过程即解决问题的步骤，面向过程的设计就好比精心设计好一条流水线，考虑周全什么时候处理什么东西

**优点**：极大的降低了程序的复杂度

**缺点**：一套流水线或者流程就是用来解决一个问题，生产汽水的流水线无法生产汽车，即便是能，也得是大改，改一个组件，牵一发而动全身

**应用场景**：一旦完成基本很少改变的场景，著名的例子有Linux內核，git，以及Apache HTTP Server等

面向对象的程序设计的核心是==对象==（上帝式思维）

特征和技能分别对应对象的数据属性和方法属性，粗略定义：对象就是变量和函数的结合体

**优点**：==解决了程序的扩展性==。对某一个对象单独修改，会立刻反映到整个体系中，如对游戏中一个人物参数的特征和技能修改都很容易

**缺点**：==可控性差==，无法向面向过程的程序设计流水线式的可以很精准的预测问题的处理流程与结果，面向对象的程序一旦开始就由对象之间的交互解决问题，即便是上帝也无法预测最终结果

**应用场景**：需求经常变化的软件，一般需求的变化都集中在用户层，互联网应用，企业内部软件，游戏等都是面向对象的程序设计大显身手的好地方

==面向对象的程序设计并不是全部。对于一个软件质量来说，面向对象的程序设计只是用来解决扩展性==

软件质量属性：成本、性能、可靠性、安全性、可维护性、可移植性、可伸缩性、==可扩展性==


### 类和对象

提示：python的class术语与c++有一定区别，与 Modula-3更像

Python中一切皆为对象，且Python3统一了类型和类的概念，类型就是类


```
 >>> dict # 类型dict就是类dict
<class 'dict'>
>>> d=dict(name='linda') # 实例化
>>> d.pop('name') # 向d发一条消息，执行d的方法pop
'linda'
```

特征即数据属性，技能即方法属性，特征与技能的结合体就一个对象

从一组对象中提取相似的部分就是类，类所有对象都具有特征和技能的结合体


### 元类分析


```


Mymeta(type):
    def __call__(self, *args, **kwargs):
        # 调用__new__方法制造对象
        obj = self.__new__(self)

        #调用__init__方法初始化对象
        self.__init__(obj, *args, **kwargs)

        # 返回对象
        return obj


class Chinese(metaclass=Mymeta):  # Mymeta('Chinese', (object,), {...})
    country = 'China'
    
    def __new(cls, *args,  **kwargs):
        return object.__new__(cls, *args,  **kwargs)

   def __init__(self, name, age):
        self.name = name
        self.age = age

c = Chinese('Linda', age=18)  # Mymeta.__call__(Chinese, 'Linda', age=18)

```


1. 先定义后使用原则 Chinese需先定义
2. 定义类Chinese三要素：类名，继承类，执行类体后的名称空间字典
    Mymeta('Chinese', (object,), {'country': 'China'})
3. 定义类 类体是需要执行
4. Chinese类体内实现 定义制造对象__new__方法的定义
5. Chinese类体内实现 初始化对象__init__方法的定义
6. Chinese() 触发 Chinese元类的__call__方法
7. Chinese元类的__call__方法：
    调用__new__方法制造对象
    调用__init__方法初始化对象
    返回对象
8. 最终申请到对象 c = Chinese('Linda', age=18)