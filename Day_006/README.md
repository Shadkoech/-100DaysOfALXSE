# Day_006

Day_006 of the #100daysof code and today I am handling python Asynchronous Comprehensions.

## Overview
Python 3.6 saw the addition of python Asynchronous Comprehensions and Asynchronous Generators. This allows the production of lists, dicts and sets with a simple and concise syntax. 
The key concepts handled include:
- `Async Comprehensions` : provide a concise syntax for asynchronously generating collections of data. They enable developers to construct asynchronous generators in a compact and readable manner, similar to list comprehensions and generator expressions. By utilizing async comprehensions, developers can express complex asynchronous operations in a succinct and expressive manner, improving code readability and maintainability.
- `Asynchronous Generators` : are coroutines that produce a sequence of values asynchronously. They are defined using the async def syntax and employ the yield statement to produce values. By leveraging asynchronous generators, developers can efficiently generate sequences of data without blocking the event loop, thus enhancing concurrency and scalability.

## Task

Files:

	- runtime.py, main.py

Write code that showcases:

- The use of Async generator
- Async Comprehensions
- Run time for four parallel comprehensions


## Outcome

In the function measure_runtime, we see that we are executing async_comprehension four times in parallel using asyncio.gather. 

- Each call to async_comprehension internally runs async_generator, which involves waiting for 1 second asynchronously per iteration. Since async_comprehension is called four times in parallel using asyncio.gather, the total time taken will be approximately 4 seconds (assuming there's no significant overhead).
- But the run time is infact 10.07 seconds instead of the anticipated 4 sec.

This is attributed to some overhead operations such as:
	- stopping coroutines
	- context switching
	- Variations in execution time due to system load, CPU performance etc

* Therefore, even though the coroutines are executed in parallel, the total runtime is slightly longer than the sum of individual runtimes due to these factors.
