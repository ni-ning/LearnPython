### 1. 插入文档

insert 如果插入数据的时候，collection还不存在时，自动创建集合
insertOne：插入一条数据
insertMany：接收数组，插入多条文档
    (*) db.student1.insertOne({"_id":"stu001", "name":"Tom", "age":25, "grade":{"chinese":80, "math":90, "english":88}})
    (*) db.student1.insertMany([
        {"_id":"stu003", "name":"Mary", "age":23, "grade":{"chinese":80, "math":90}},
        {"_id":"stu004", "name":"Mike", "age":25, "grade":{"chinese":80, "math":90, "english":88}},
    ])
    (*) 统一的形式：insert 插入文档，也可以是文档的数组，就是insertOne与insertMany的统一

### 2. 查询文档  
  数据源参考数据脚本
  
    (*) 基本查询
        (1) 查询所有的员工信息
            db.emp.find()
        (2) 查询职位为经理的员工
            db.emp.find({"job": "MANAGER"})
        (3) 操作操作 $in和$or
            查询职位是MANAGER或者CLERK的员工信息
            db.emp.find({"job":{"$in":["MANAGER", "CLERK]}})
            db.emp.find({"$or":[{"job":"MANAGER"},{"job":"CLERK"}]})
        (4) 查询10号的部门工资大于2000的员工
            db.emp.find({"sal":{"$gt":2000}, "deptno":10})
    
    (*) 嵌套查询
        (1) 查询语文是81分，英语是88分的文档
            db.student2.find({"grade":{"chinese":81, "english":88}})  --> 只匹配只有语文和英语的文档
        (2) 查询语文是81分，数学90分，英语是88分的文档
            db.student2.find({"grade":{"chinese":81, "math":90, "english":88}}) --> 顺序也要一直
            
            小结：如果是相等查询，保证匹配所有的field，顺序也要一致
        (3) 查询嵌套文档中的一个列：查询数学成绩是82分的文档
            db.student2.find({"grade.math":82})
        (4) 使用比较运算符：查询英语成绩大于88分文档
            db.student2.find({"grade.english":{"$gt":88}})
        (5) 使用AND运算符：查询英语成绩大于88分文档，语文大于85分文档
            db.student2.find({"grade.english":{"$gt":88}, "grade.chinese":{"$gt":85}})
    
    (*) 查询数组的文档
        (1) 查询所有有Hadoop和Java的文档
            db.studentbook.find({"books":["Hadoop", "Java"]})   --> 没有结果
            正确：
            db.studentbook.find({"books":{"$all":["Hadoop", "Java"]}})
        (2) 跟查询嵌套的文档一样，匹配每个元素，顺序也要一样
            db.studentbook.find({"books":["Hadoop", "Java", "NoSQL"]})
    
    (*) 查询数组中嵌套的文档
        (1) 查询Java有4本的文档
            db.studentbook1.find({"books":{"bookname": "Java", "quantity": 4}})
        
        (2) 指定查询的条件：查询数组中第一个元素大于等于3本的文档
            db.studentbook1.find({"books.0.quantity":{"$gte":3}})
            
            如果不知道field的位置：查询文档中至少有一个quantity的值大于1
            db.studentbook1.find({"books.quantitiy":{"$gt":3}})
        
        (3) 查询Java有4本的文档
            db.studentboo1.find({"books":{"$elemMatch":{"bookname":"Java", "quantity":4}}})
        
    (*) 查询空值null或者缺失值
        (1) 查询值为null的文档
            db.student3.find({"age":null})  --> 返回2条记录
        
        (2) 只返回null的记录：BSON表示null的为{"$type":10}
            db.student3.find({"age":{"$type":10}})
        
        (3) 检查是否缺失某个列：{"$exists": bool}
            db.student3.find({"age":{"$exists": false}})
            db.student3.find({"age":{"$exists": true}})
    
    (*) 使用游标
        db.collection.find()  ---> 返回一个cursor：如果使用cursor，使用迭代器，默认返回20条文档
        (1) 定义游标
        var mycursor = db.emp.find()
        mycursor
        (2) 使用游标访问文档
        var mycursor = db.emp.find()
        while(mycursor.hasNext()){
            printjson(mycursor.next())
        }
        (3) 游标转数组
        var mycursor = db.emp.find()
        var myarray = mycursor.toArray()
        var mydoc = myarray[0]
        (4) 分页查询：skip和limit，每页显示5条
         第一页：var mycursor = db.emp.find().limit(5)
         第二页：var mycursor = db.emp.find().limit(5).skip(5)

### 3. 更新文档：updateOne和updateMany
    (1) 更新 7839的薪水  --> 9000
        db.emp.updateOne({"_id":7839}, {"$set":{"sal":9000}})     --> updateOne({}, {})
    (2) 更新多条数据：更新10部门的员工薪水，加100块钱
        db.emp.updateMany({"deptno":{"$eq":10}}, {"$set":{"sal":"sal"+100}}) --> 错误
        db.emp.updateMany({"deptno":{"$eq":10}}, {"$inc":{"sal":100}})
    (3) 官方文档
        https://docs.mongodb.com/manual/reference/method/db.collection.updateOne/#db.collection.updateOne
    
### 4. 删除文档
        
 
    