# Day_048

- #100daysofalxse 
- #DoingHardThings
- #DailyGrowth

Today I continued to learn and build on Node.JS
I handled express.js in particular which is a minimal and flexible Node.js web application framework that provides a robust set of features for web and mobile applications. APIs.
I created simple servers on the same as seen in the file:

## Materials 
- [Getting started](https://nodejs.org/en/learn/getting-started/introduction-to-nodejs)
- [Process Doc](https://node.readthedocs.io/en/latest/api/process/)
- [Child processes](https://nodejs.org/api/child_process.html)

## Objectives
- Run JavaScript using NodeJS
- Utilize NodeJS modules effectively
- Read and manipulate files synchronously and asynchronously
- Access command line arguments and environment variables using the Process API
- Create HTTP servers using NodeJS and ExpressJS
- Implement advanced routes with ExpressJS
- Utilize ES6 features with NodeJS, including Babel-node
- Develop faster using Nodemon


## Task
File:
    - http_express.js
In a file named http_express.js, recreate the small HTTP server using Express:

It should be assigned to the variable app and this one must be exported
HTTP server should listen on port 1245
It should return plain text
When the URL path is /, it should display Hello Holberton School! in the page body
When the URL path is /students, it should display This is the list of our students followed by the same content as the file 3-read_file_async.js (with and without the database) - the name of the database must be passed as argument of the file
CSV file can contain empty lines (at the end) - and they are not a valid student!
