测试celery在使用redis作为broker时内存的使用情况
========

celery支持将task执行后的结果存入backend,见[doc](http://celery.readthedocs.org/en/latest/configuration.html#task-result-backend-settings)的`CELERY_RESULT_BACKEND`项)，支持的backend有）database,	cache,mongodb,redis,ampq,cassandra等等，这里将分别对

* `使用redis作为result backend` 
* `关闭result backend`

两种情况下内存的使用情况

# 软硬件信息
* 内存:10G
* CPU：Intel Core i5 2.4GHz
* OS X ：10.9.3
* redis:2.6.16 
* celery:3.1.16
* python:2.7.3


# 运行测试脚本
需要先安装`redis server`

```
setup environment
$ ./setupenv.sh

run producer
$ python producer.py  -n 1000 

run celery
$./run_celeryd.sh

```

# 内存使用情况

### 关闭result backend

set `CELERY_RESULT_BACKEND = None` 

Tasks|Mem(new)|Mem(done)|Status
---|---|
1w|8.3M|1.17M|new
10W|74.26M|1.17M|new
50W|367.23M|1.02M|new

### 开启result backend

set `CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/2"` 

Tasks|Mem(new)|Mem(done)|Status
---|---|
1w|8.3M|5.82M|new
10W|74.26M|28.75M|new
50W|367.23M|149.44M|new

