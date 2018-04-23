#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
对MongoEngine的ORM中 CollectionModel.objects.aggregate()进行封装
"""


class AggregateUtilMixin(object):

    def skip(self, skip):
        self.aggregate_pipeline.append({"$skip": skip})
        return self

    def limit(self, limit):
        self.aggregate_pipeline.append({"$limit": limit})
        return self

    def group(self, **group):
        self.aggregate_pipeline.append({"$group": group})
        return self

    def unwind(self, unwind):
        self.aggregate_pipeline.append({"$unwind": unwind})
        return self

    def project(self, **project):
        self.aggregate_pipeline.append({"$project": project})
        return self

    def sort(self, **sort):
        self.aggregate_pipeline.append({"$sort": sort})
        return self

    def match(self, **match):
        self.aggregate_pipeline.append({"$match": match})
        return self

    def lookup(self, **lookup):
        self.aggregate_pipeline.append({"$lookup": lookup})
        return self

    def count(self):
        c = {"$group": {"_id": None, "count": {"$sum": 1}}}
        self.aggregate_pipeline.append(c)
        res = list(self.query())
        self.aggregate_pipeline.pop()
        return res[0]['count'] if len(res) else 0

    def __getitem__(self, item):
        assert isinstance(item, slice)
        self.aggregate_pipeline.append({"$skip": item.start})
        self.aggregate_pipeline.append({"$limit": item.stop - item.start})
        return self

    def __iter__(self):
        for item in list(self.query()):
            yield item


class AggregateQuery(object):
    def __init__(self):
        super(AggregateQuery, self).__init__()
        self.aggregate_pipeline = []

    def query(self, aggregate_pipeline=None):
        raise NotImplemented


if __name__ == '__main__':

    from mongoengine import *
    import datetime

    # 配置信息，实际开发中须提取为单独文件 settings.py or services.py
    MONGO = {
        'test': {
            'name': 'test',
            'host': '192.168.4.5',
            'port': 27017
        }
    }

    # 连接MongoDB, 同connect()
    for alias, attrs in MONGO.items():
        register_connection(alias, **attrs)

    # 定义ORM，实际开发中须提取为单独目录下文件 models.py
    class Address(EmbeddedDocument):
        province = StringField()
        city = StringField()


    class Custom(DynamicDocument):
        meta = {
            'db_alias': 'test',
            'collection': 'custom',
            'indexes': ['name']
        }
        name = StringField(required=True)
        age = IntField()
        sex = BooleanField(default=True)
        hobbies = ListField()
        address = EmbeddedDocumentField(Address, default=Address)
        created = DateTimeField(default=datetime.datetime.now)


    class OperationRecord(DynamicDocument):
        meta = {
            'db_alias': 'test',
            'collection': 'operation_record',
            'indexes': ['custom_id', 'operate_type']
        }
        custom_id = ObjectIdField()
        operator = StringField()
        operate_type = StringField()
        create_time = DateTimeField(default=datetime.datetime.now)

    # 添加测试数据 Custom
    # c = Custom('Linda')
    # c.age = 18
    # c.sex = False
    # c.hobbies = ['reading', 'running', 'dancing']
    # c.address = Address('Beijing', 'Beijing')
    # c.save()

    # Custom('Catherine', 18, False, ['buying, buying'], Address('Jiangsu', 'nanjing')).save()
    # Custom('Test1', 18, False, ['sleeping', 'running'], Address('Beijing', 'Beijing')).save()
    # Custom('Test2', 28, False, ['smiling', 'jogging'], Address('Beijing', 'Beijing')).save()
    # Custom('Test3', 88, False, ['shooting'], Address('Beijing', 'Beijing')).save()

    # 添加测试数据 OperationRecord
    # OperationRecord('5add8a41c1f80e30843a2568', '5add8a41c1f80e30843a2568', '分配').save()
    # OperationRecord('5add8fd5c1f80e17c85759ef', '5add8fd5c1f80e17c85759ef', '分配').save()
    # OperationRecord('5add9052c1f80e1bd80e2924', '5add9052c1f80e1bd80e2924', '分配').save()
    # OperationRecord('5add9052c1f80e1bd80e2925', '5add9052c1f80e1bd80e2925', '分配').save()
    # OperationRecord('5add9052c1f80e1bd80e2926', '5add9052c1f80e1bd80e2926', '分配').save()


    class OperationRecordQuery(AggregateQuery, AggregateUtilMixin):
        def __init__(self):
            super(OperationRecordQuery, self).__init__()

        @staticmethod
        def get_collection_name():
            return OperationRecord._get_collection_name()

        def query(self, aggregate_pipeline=None):
            if not aggregate_pipeline:
                aggregate_pipeline = self.aggregate_pipeline
            return OperationRecord.objects.aggregate(*aggregate_pipeline)

        # 缓存个数
        # def cache_count(self):
        #     def hash_key():
        #         query_dict = {'collection': self.get_collection_name(),
        #                       'query': self.aggregate_pipline}
        #         return to_hash(query_dict)
        #
        #     def get_count():
        #         return self.count()
        #
        #     return cached(key=hash_key, timeout=3600)(get_count)()

    # 结合flask.request获取相关 筛选、搜索、排序、分页、权限等信息
    query_con, start, end = {}, 0, 2
    query_con.update({'operate_type': '分配'})
    sort_param = {'create_time': -1}

    """
    1. 表operation_record 去关联 表custom ，$lookup实现
    会在db.operation_record.aggregate({"$lookup":{xxxx}})，聚合结果每条文档记录中增加了一个字段 "operation_custom"
    "operation_custom" : [ 
        {
            "_id" : ObjectId("5add8a41c1f80e30843a2568"),
            "name" : "Linda",
            "age" : 18,
            "sex" : false,
            "hobbies" : [ 
                "reading", 
                "running", 
                "dancing"
            ],
            "address" : {
                "province" : "Beijing",
                "city" : "Beijing"
            },
            "created" : ISODate("2018-04-23T15:24:47.945Z")
        }
    
    2. "operation_custom":[] 拆分为 "operation_custom":{}
    db.operation_record.aggregate({"$lookup":{xxxx}}, {"$unwind":"$operation_custom"})
    
    """
    lookup = {
        'from': Custom._get_collection_name(),
        'localField': 'custom_id',
        'foreignField': '_id',
        'as': 'operation_custom'
    }

    # 基本核心查询
    query = OperationRecordQuery().match(**query_con).sort(**sort_param).\
        lookup(**lookup).unwind("$operation_custom")

    # 级联查询
    sex = {'operation_custom.sex': True}
    query = query.match(**sex)

    # 分页
    query = query[start:end]

    # 封装输出
    for item in query:
        print(item)
