 #### 1. Python介绍  
**-程序员减少开发成本**

创业性公司  - Python使用较多，开发效率高  
老牌大公司  - 有部门使用

**-应用领域**

- 自动化运维

    -- 安装Linux 自带 Python
    
    -- 现成的库较多，开发效率高
- 自动化测试  
- 大数据分析  
- 爬虫  
- Web

#### 2. Python和其他语言对比
&nbsp;&nbsp;&nbsp;&nbsp;- C: 机器码   
&nbsp;&nbsp;&nbsp;&nbsp;- 其他高级语言：字节码 -> 机器码

go语言擅长处理网络并发


### 3. Python的种类
&nbsp;&nbsp;&nbsp;&nbsp;- CPython: 代码  ->  C字节码 -> 机器码(一行一行)  
&nbsp;&nbsp;&nbsp;&nbsp;- PyPy: 代码  ->  C字节码 -> 机器码(全部执行完 -> 再执行，编译需要时间)  
&nbsp;&nbsp;&nbsp;&nbsp;- 其他Python:  代码  ->  其他字节码  ->  机器码(一行一行)

学习时只需学习Python规则即可

### 4.Python基础
**-Python规则**
- 安装：Python解释器
- 写程序 C:\python.exe  test.py

    a. 打开文件，读取文件内容  
    b. 词法分析，语法分析   
    c. 字节码  
    d. 机器码

**-解释器**  

Windows下:   
- C:\python.exe  test.py  

Linux下:    
- 头部增加注释：  #!/usr/bin/python  (Linux会自动切换到相应的解释器来解释该脚本)    
- 更改可执行权限： chmod 755 test.py  
- 执行代码： ./test.py



**-编码**

英文： ASCII   
万国码(至少16位，unicode)：英文 2字节、中文 3个字节，8位1字节往后排 -- > 万国的编码  
utf-8：对万国码的压缩， 英文1字节，中文3字节  

中文编码相关：   
gbk，gb2312  
utf-8:  3个字节，24位  
gbk:    2个字节，16位

总结：

- utf-8通用格式；以某种编码格式存储的文件，就该用相应编码来读，否则会出现乱码
- 脚本开头 -*- coding:utf-8 -*-   告诉解释器以utf-8的格式来解释(存储时为utf-8)，则可以正常读取

Python编码相关：  
&nbsp;&nbsp;&nbsp;&nbsp;-- 文件存储编码  
&nbsp;&nbsp;&nbsp;&nbsp;-- Python解释器编码(Python3默认 utf-8，想以其他方式解释，请指定 # -*- coding:utf-8 -*- )


#### 5.预编译字节码
.pyc 编译完之后的字节码

#### 6. 变量
        
&nbsp;&nbsp;&nbsp;&nbsp;- 字母  
&nbsp;&nbsp;&nbsp;&nbsp;- 数字（不能开头）  
&nbsp;&nbsp;&nbsp;&nbsp;- 下划线  
&nbsp;&nbsp;&nbsp;&nbsp;-   不能使用python内置关键字

PS: 下划线分割

#### 7. 输入输出


```
v = input("请输入变量值： ")
import getpass
pwd = getpass.getpass("请输入密码：")
print(pwd)
```



#### 8. 条件语句

场景一
if xx:
    pass

场景二
if xx:
    pass
else:
    pass

场景三
if xx:
    pass
elif xx:
    pass
else:
   pass

#### 9. 循环语句
while 条件:  
&nbsp;&nbsp;&nbsp;&nbsp;continue    # 立即开始下次循环  
&nbsp;&nbsp;&nbsp;&nbsp;break       # 跳出所有循环

#### 10. Python 数据类型
**a. 整数**
- 创建
a = 123
a = int(123)
- 转换
age = '18'
new_age = int(age)

**b. 布尔值**
- 创建
a = True
b = False
- 转换
数字转换时，只有0是False，其他都为True
a = bool(1)  True b = bool(0)  False  
字符串转换时，只要“”为False，“ ” 为True，其他都为True

**c. 字符串**  
-创建  

```
a = "alex"  
a = str('alex')
```


-转换  

```
age = 18  
new_age = str(age)
```


-字符串拼接  

```
"str1" + "str2"
 "我叫 %s, 今年 %s" % ("alex",18)   # 占位符，有顺序
```


-判断子序列是否在其中  

```
content = "Alex前几天去泰国玩，一不小心染上了病"
if "前几天" in content
    print(True)
else:
    print(False)
```


-移除空白  

```
val = '   alex   '
print(val.strip())
print(val.lstrip())
print(val)
```


-分割  

```
user_info = "alex|sb123|9"  
v1 = user_info.split("|", 1)  
print(v1)  
v2 = user_info.rsplit("|", 1)  
print(v2)

-长度, python3 按字符
```
  

```
val = '杰李sb'  
print(len(val))
```

-索引 按字符    
```
val = '李杰sb'  
print(val[3])   
i = 0
while i < len(val):
    print(val[i])
    i += 1
```

-切片

```
name = '我叫李杰，今年18岁，我在说谎！'
print(name[0:2])
print(name[5:9])
print(name[5:])
print(name[5:-1])
print(name[0:10:2])
print(name[0::2])
print(name[-2:])
```

**d.列表**

创建：

```
a = ['alex', '狗', 'eric', 123]
b = list(['alex', '狗', 'eric', 123])
```

-   in    'alex' in a
-   长度  len(a)
-   索引  a[0]
-   切片  a[0:]
-   追加  a.append('xxoo')
-   插入  a.insert(0, '牛')
-   删除  a.remove[value]   del a[0]
-   更新  a[0] = new_value
```
# for 循环
fro item in a:
print(item)
```


**e.字典**
- 创建

```
dict1 = {
    'name': 'alex',
    'password': 123456
}
```

- 操作

```
# 根据索引，获取值
name = dict1['name']
print(name)

# 无：增加；有：修改
dict1['age'] = 18
print(dict1)

删除
del dict1['name']
print(dict1)

# for循环
for k, v in dict1.items():
    print(k, v)

for k in dict1.keys():
    print(k)

for v in dict1.values():
    print(v)
```
PS：列表和字典相互嵌套

