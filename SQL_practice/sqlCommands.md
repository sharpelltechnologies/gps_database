# Simple SQL Commands 

## Create/Set
create new database ------- `create database [db]`
set current db ------------ `use [db];`

## Insert
insert row into table ----- `INSERT INTO [tbl]([col1], [col2], ...) 
                             VALUES([val1], [val2], ... )`

## Reading 
show all databases -------- `show databases;`
show current db ----------- `select database();`

show all tables ----------- `show tables;`
show tbl structure -------- `describe [tbl];`
select records ------------ `SELECT * FROM [tbl];`
select parts of records --- `SELECT [colA], [colB] FROM [tbl];`
select parts of records2 -- `SELECT * FROM [tbl] WHERE [ predicate ];`
order records ------------- `SELECT * FROM [tbl] ORDER BY [col];`
count records ------------- `SELECT COUNT ([col]) FROM [tbl];`

show IP of MySQL host ----- `SHOW VARIABLES WHERE Variable_name = 'hostname';`

