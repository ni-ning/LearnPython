### 1. 启动 mongo shell
启动：mongo
参数：--username 用户名
      --password 密码
      --host
      --port
简写的方式： mongo -u *** -p *** -host *** -port ***
帮助信息： mongo --help
可以在mongo shell中使用外部的编辑器: vim
    (*) 设置环境变量 export EDITOR=vim
    (*) mongo shell中定义 function myFunction(){}
    (*) edit myFunction  进入vim编辑器，编辑，保存，退出
    (*) mongo shell中执行 myFunction()

### 2. mongo shell启动配置文件(shell, not mongod)
    (*) 在当前用户的家目录下： ~/.mongorc.js
    (*) 示例一：显示当前发出命令的数量
        vim ~/.mongorc.js
        cmdCount=1;
        prompt=function(){
            return "mongo " + (cmdCount++) + " >";
        }
    (*) 示例二：显示数据库名称和主机名称
        vim ~/.mongorc.js
        host=db.serverStatus().host;
        cmdCount=1;
        prompt=function(){
            return db + "@" + host + " " +(cmdCount++) + " >";
        }

### 3. mongo shell的基本操作
    show dbs;
    use mydemo1;
    db.test1.insertOne({x:1})
    show tables;
    show collections;

### 4. mongo shell数据类型：字符串、整型、布尔值、浮点数、时间
    (1) 日期类型 Date
        Date(): 表示当前时间，插入一个字符串类型，如 Sat Apr 21 2018 11:34:51 GMT+0800 (CST)
        new Date(): 插入的是isodate类型，表示的是格林威治标准时间，如ISODate("2018-04-21T03:34:59.361Z")
        ISODate(): 类似 new Date()，如ISODate("2018-04-21T03:34:59.361Z")
    (2) ObjectId: 当插入数据的时候，自动生成一个字段 "_id" --> 相当于主键，ObjectId("5adab023eedb6b279a2ecb29")
        ObjectId 是一个12字节的BSON类型的字符串，易于分布式
    (3) 表示数字的时候，注意问题
        NumberInt：表示32位整数
        NumberDecimal：支持34位小数
        Double：数字默认类型

        建立测试数据
        {"_id":1, "val": NumberDecimal("9.99"), "description": "Decimal"}
        {"_id":2, "val": 9.99, "description": "Double"}
        {"_id":3, "val": 10, "description": "Double"}
        {"_id":4, "val": NumberLong(10), "description": "Long"}
        {"_id":5, "val": NumberDecimal("10.0"), "description": "Decimal"}

        执行一下查询
        (1) 条件：{"val": 9.99}
        { "_id" : 2, "val" : 9.99, "description" : "Double" }
        原因：默认9.99是Double
        (2) 条件：{"val": NumberDecimal("9.99")}
        { "_id" : 1, "val" : NumberDecimal("9.99"), "description" : "Decimal" }
        (3) 条件：{"val": 10}
        { "_id" : 3, "val" : 10, "description" : "Double" }
        { "_id" : 4, "val" : NumberLong(10), "description" : "Long" }
        { "_id" : 5, "val" : NumberDecimal("10.0"), "description" : "Decimal" }
        原因：对于整数10的匹配，将匹配所有的数据类型是10
        (4) 条件：{"val": NumberDecimal("10")}
        { "_id" : 3, "val" : 10, "description" : "Double" }
        { "_id" : 4, "val" : NumberLong(10), "description" : "Long" }
        { "_id" : 5, "val" : NumberDecimal("10.0"), "description" : "Decimal" }

### 5. 使用MongoDB Web的控制台：需要在启动MongoDB的时候，指定参数 --httpinterface
        社区版没有该选项
