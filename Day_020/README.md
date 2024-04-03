# Day_020

Day_020 of the #100daysofalxse #DoingHardThings

Today was all about Caching.

## Overview
Caching is an amazing concept that enables the creation of fast and responsive applications. It is simply the process of storing data close to where it is needed for fast access compared to its expensive origin each time a request comes in. 

The issue however is, cache memory is finite. It gets filled up fast and therefore, we need to know what to hold and what to discard in order to optimize the storage. Resources frequently needed and accessed are held longer compared to those accessed just once.

## Algorithms
Well, there are a number of algorithms that I went through today that can achieve the above. They include:

### First-In/First-Out (FIFO)
Evicts the oldest of the entries
Newer entries are most likely to be reused

### Last-In/First-Out (LIFO)
Evicts the latest of the entries
Older entries are most likely to be reused

### Least Recently Used (LRU)
Evicts the least recently used entry
Recently used entries are most likely to be reused

### Most Recently Used (MRU)
Evicts the most recently used entry
Least recently used entries are most likely to be reused

### Least Frequently Used (LFU)
Evicts the least often accessed entry
Entries with a lot of hits are more likely to be reused


## Tasks
Two files inheriting from a basic cache
Implements:
- FIFO
- LIFO