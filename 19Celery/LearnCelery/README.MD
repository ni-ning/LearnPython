### 程序介绍


celery是一个基于python开发的分布式异步消息队列，轻松实现任务的异步处理

- 分布式任务
- 定时任务

### 目录结构

```
LearnCelery
   |-- app
        |-- tasks.py
        |-- models.py
   |-- LearnCelery
        |-- __init__.py
        |-- celery.py
        |-- settings.py
   |README.md    
```


### 使用说明

1. 启动Django   python3 manage.py runserver 0.0.0.0:8080

2. 启动worker   celery -A LearnCelery worker -l debug

3. 启动beat     celery -A LearnCelery beat -l info -S django