## SQL语句
### 操作文件夹(库)
#### 增
+ create database db1 charset utf8;
#### 查
+ show create database db1;
+ show databases;
#### 改
+ alter database db1 charset gbk;
####删
+ drop database db1;


### 操作文件(表)
+ 切换文件夹  use db1; 
+ 查看当前文件夹 select database();
#### 增
+ create table t1(id int,name char);
    - t1.frm  # 表结构
    - t1.ibd  # 表内容
#### 查
+ show create table t1;
+ show tables;
+ desc t1;
#### 改
+ alter table t1 modify name char(6);      # 修改字段类型
+ alter table t1 change name NAME char(7)  # 修改字段名
#### 删
+ drop table t1;

### 操作文件内容(记录)
#### 增
+ insert into t1(id, name) values(1, 'linda1'),(2,'linda2'),(3, 'linda3')
+ insert into t1 values(xx,xx),(xx,xx)
#### 查
+ select id,name from db1.t1;
#### 改
+ update db1.t1 set name="SB";
+ update db1.t1 set name="alex" where id=2
#### 删
+ delete from db1.t1;
+ delete from db1.t1 where id=2