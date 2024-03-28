#!/usr/bin/env python3
"""
Python module that connects and runs multiple Redis operations
on a number of data types"""

import redis

# Connect to Redis
redis_host = 'localhost'
redis_port = 6379
redis_password = None
redis_db = 0

r = redis.Redis(host=redis_host, port=redis_port, password=redis_password, db=redis_db)

# Basic operations
r.set('mykey', 'Hello Redis!')
value = r.get('mykey')
print(value.decode('utf-8'))

# Incrementing a value
r.set('counter', 0)
r.incr('counter')
print(r.get('counter'))

# Working with lists
r.lpush('mylist', 'item1')
r.lpush('mylist', 'item2')
r.lpush('mylist', 'item3')

print(r.lrange('mylist', 0, -1))

# Working with sets
r.sadd('myset', 'a')
r.sadd('myset', 'b')
r.sadd('myset', 'c')

print(r.smembers('myset'))

# Working with hashes
r.hset('myhash', 'name', 'John')
r.hset('myhash', 'age', 30)

print(r.hgetall('myhash'))
