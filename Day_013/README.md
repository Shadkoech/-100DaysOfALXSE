# Day_013

Day_013 of the #100daysofalxse
#DoingHardThings

Today I continued to focus on backend storage system. I read and exercised on Redis (Remote Dictionary Service)

## Description
Remote Dictionary Service (Redis) is a high-performance in-memory data structure store that is widely used as a caching solution, database and a message broker due to its speed, versatility, and rich feature set.

![Redis Logo](image.png)


## Task
I handled a task that covered the following:
- Redis installation
- Practicing on Redis syntax, protocol and design on redis-cli
- Mastering redis-py



File

    - web.py
Implement a get_page function (prototype: def get_page(url: str) -> str:). The core of the function is very simple. It uses the requests module to obtain the HTML content of a particular URL and returns it.
* Start in a new file named web.py and do not reuse the code written in exercise.py.
* Inside get_page track how many times a particular URL was accessed in the key "count:{url}" and cache the result with an expiration time of 10 seconds.

Tip: Use http://slowwly.robertomurray.co.uk to simulate a slow response and test your caching.