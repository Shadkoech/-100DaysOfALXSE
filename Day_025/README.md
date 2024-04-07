# Day_025

Day_025 of #100DaysofALXSE Challenge
#DoingHardThings
#DailyGrowth

Today, I went through a very interesting concept called memoization.

## Overview
Memoization is actually an optimization technique that is used to speed up the execution time of functions by caching the results of expensive function calls and returning the catched result when the same input occurs again. 
This technique is very useful and comes in handy when dealing with recursive algorithms where the same inputs are computed repeatedly.

Actual uses cases
- When you have a slow function but you need to get the same result over and over instantaneously
- When fetching external resources say from a link. Memoization helps skip the need of having to make calls to the servers over and over on the same results
- Used in Dynamic programming. i.e a recursive function that calls itself over and over using the same input and you have actually memoized those same inputs. 



## Tasks

### Square function
File:

    - square.js
File that instantaneously give the result (square) of a very large number using memoization. 
The result of the function would take longer times to be computed but in this case since it is cached, a consecutive call: second, third etc is immediately given

### The Fibonacci series
File:

    - Fib.js
Using memoization to speed up the result of fibanacci series
With Fiboncci, the result of very large numbers take time to be executed since any given number is the result of the sum of two of it's predecessors.
Instead of having to recalculate these sums over and over, we can memoize the result of numbers as we go up such that huge numbers needs to just refer and pick the result of fibonacci output of numbers below it