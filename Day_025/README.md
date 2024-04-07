# Day_025

Day_025 of #100DaysofALXSE Challenge
#DoingHardThings
#DailyGrowth

Today, I went through a very interesting concept called memoization.

## Overview
Memoization is actually an optimization technique that is used to speed up the execution time of functions by caching the results of expensive function calls and returning the catched result when the same input occurs again. 
This technique is very useful and comes in handy when dealing with recursive algorithms where the same inputs are computed repeatedly.


## Tasks

### Square function
File:

    - square.js
File that instantaneously give the result (square) of a very large number using memoization. 
The result of the function would take longer times to be computed but in this case since it is cached, a consecutive call: second, third etc is immediately given