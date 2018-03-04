## MySQL
套接字管理数据库软件服务端、客户端
+ 支持并发，允许多用户访问
+ 并发意味着竞争，要处理锁的问题
+ 性能、安全问题
+ ......

### 一、 数据库相关概念

#### 1. 数据库服务器：运行数据库管理软件的计算机

#### 2. 数据库管理软件：mysql、oracle、db2、sqlserver
mysql就是一个基于socket编写的C/S架构的软件

数据库管理软件分类
+ 关系型数据库，需要表结构(字段名、数据类型、约束等)，如sqllite，db2，oracle，sqlserver，MySQL等，sql语句通用
+ 非关系型数据库，没有表结构，以key-value存储，没有表结构，如mongodb，redis，memcache

#### 3. 库：文件夹

#### 4. 表：文件
单纯文本中一条记录，还不能完整描述一个事物特征

#### 5. 记录：事物一些列典型特征：Jonathan, age, 18, UTC

#### 6. 数据：描述事物特征的符号
人让计算机来干活，计算机得能理解人的想法，数据是很好的中间载体，所以我们需要数据

### 二、使用MySQL

#### 2.1 安装
Windows 5.6即可
http://dev.mysql.com/downloads/mysql/

tasklist | findstr mysql
taskkill /F /PID  <pid>

制作系统服务  mysqld --install 
移除系统服务  mysqld --remove
net start MySQL  # 关闭服务
net stop MySQL   # 启动服务

CentOS7:  
+ yum -y install mariadb-server mariadb
+ systemctl start mariadb

CentOS6:  yum -y install mysql-server mysql
#### 2.2 简单使用
mysql
select user();

mysql -uroot -p    enter 默认无密码
select user(); 

#### 2.2 设置密码
mysqladmin -uroot -p password "nining123456"
mysqladmin -uroot -pnining123456 "root@123456"

#### 2.3 找回密码
+ 跳过授权表启动服务  mysqld --skip-grant-tables
+ 启动root mysql -uroot -p
+ 修改密码 update mysql.user set password=password("123456") where user="root" and host="localhost";
+ 刷新授权表 flush privileges;
+ 退出并关闭服务 exit&taskill
+ 重新启动数据库服务 mysqld

#### 2.4 登录远程服务
mysql -uroot -p123456 -h 127.0.0.1 -P 3306

#### 2.5 统一字符编码
client> \s   # 查看信息
```
[mysqld]   # 服务端配置
character-set-server=utf8
collation-server=utf8_general_ci
[client]  # 所有客户端配置
default-character-set=utf8
[mysql]   # mysql命令行配置
default-character-set=utf8
```