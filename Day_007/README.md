# Day_007

Day_007 of the #100daysof code and today I recapped on the basics of MySQL

## Overview

Some of the fundamental concepts I came across include:

- SQL Syntax and Querying
- Creating users and assigning permissions
- Database Design and Normalization
- MySQL Data Types
- Basic CRUD Operations
- Joins: Inner, Outer, Cross, and Self Joins


## Task

On the section of the tasks, I reviewed the whole project on introduction to MySQL in order to refresh my memory on the basics before going into advanced.
Here is the link to my previously handled concepts:

One notable inclusive task I came across include the following:

### Task 1:

File:

	- create_read_user.sql
Write a script that creates the database hbtn_0d_2 and the user user_0d_2.
- user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
- The user_0d_2 password should be set to user_0d_2_pwd
- If the database hbtn_0d_2 already exists, your script should not fail
- If the user user_0d_2 already exists, your script should not fail


### Task 2:

File:

	- cities_by_state_join.sql
Write a script that lists all cities contained in the database hbtn_0d_usa.
- Each record should display: cities.id - cities.name - states.name
- Results must be sorted in ascending order by cities.id
- You can use only one SELECT statement
- The database name will be passed as an argument of the mysql command
