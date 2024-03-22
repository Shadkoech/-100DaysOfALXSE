# Day_008

Day_008 of the #100daysofalxse
Today I went ahead and built on what I did on day 7 and advanced on MySQL.

## Overview

Advanced concepts that I came across

- Creating tables with constraints
- Optimizing queries by adding indexes
- Implementing stored procedures and functions
- Implementing views
- Implementing triggers




## Task

I handled the above concepts through a number of tasks. The cumulative tasks are in this repository in the following link:

	- https://github.com/Shadkoech/alx-backend-storage/tree/master/0x00-MySQL_Advanced

One notable inclusive task I came across include the following:

### Task 1:

File: 

	- bonus.sql
Write a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.

Requirements:
- Procedure AddBonus is taking 3 inputs (in this order):
- user_id, a users.id value (you can assume user_id is linked to an existing users)
- project_name, a new or already exists projects - if no projects.name found in the table, you should create it
- score, the score value for the correction


### Task 2:

File:

	- 2-fans.sql
Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans

Requirements:
- Import this table dump: metal_bands.sql.zip
- Column names must be: origin and nb_fans
- Your script can be executed on any database