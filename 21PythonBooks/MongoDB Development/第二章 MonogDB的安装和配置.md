### 1. MongoDB的安装与配置
```
sudo apt-get remove mongo*
cd /root/training
wget mongodb-linux-x86_64-ubuntu1404-3.6.4.tgz
tar -zxvf mongodb-linux-x86_64-ubuntu1404-3.6.4.tgz -C /root/training
export PATH=/root/training/mongodb-linux-x86_64-enterprise-ubuntu1404-3.7.5/bin:$PATH    临时生效
```

```mongod  提示/data/db不存在
mkdir -p /data/db
mongod --dbpath=/data/db
启动成功提示
waiting for connections on port 27017
```

错误信息
mongod: error while loading shared libraries: libnetsnmpmibs.so.30


方法二：[官方ubuntu](https://docs.mongodb.com/manual/tutorial/install-mongodb-enterprise-on-ubuntu/)

```
/var/lib/mongodb  # 数据库文件
/var/log/mongodb  # 日志文件
/etc/mongod.conf  # mongod配置文件

sudo service mongod start
sudo service mongod stop
```


### 2. MongoDB的体系结构
* 一个MongoDB Server: 实例和多个数据库(1:N)
* 存储结构
    1. 逻辑存储结构：数据库(database)、表(collection)、记录(document)
    2. 物理存储结构：
        * --dbpath=/data/db 指定数据库存储的位置
        * MongDB的物理存储的文件
            * 命名空间文件    后缀.ns 大小 16M
            * 数据文件       后缀0,1,2,3  
                            大小  
                            0 --> 16M   
                            1 --> 32M  
                            2 --> 64M  
                            最大 2G
            * 日志文件 存储的位置可能不一样
                * 直接存储在操作系统中
                    * 系统日志文件：记录的是系统的启动信息，告警信息等等
                    * journal日志文件：重做日志，即redo日志，用于恢复
                * 存储在集合(collection)中
                     * oplog：复制操作的日志(只在：主从复制的功能)
                     * 慢查询的日志(需要单独配置)：一般在生成系统中，大于200毫秒的日志                     
    3. 注意：
        * 从3.2版本后，MongoDB的默认的数据引擎，wiredTiger
        * 早期版本 内存映射，可以指定参数 --storageEngine=mmapv1
        * 新版本：数据文件大小从64开始
           
                     
                     
                                
    


 
 
 


