-- Chapter 1: Retrieving Records
-- 1.3 where
select * 
    from emp
    where deptno = 10
    or comm is not null
    or sal <= 2000 and deptno=20

select *
    from emp
    where (deptno = 10
        or comm is not null
        or sal <= 2000)
    and deptno=20
      
-- 1.4
select ename, deptno, sal 
from emp

-- 1.5 alias
select sal as salary, comm as commission 
from emp

-- 1.6 WHERE
-- fail: cannot reference alias names in the WHERE clause
-- WHERE clause is evaluated before the SELECT, so salary is not in the table yet
-- FROM clause is evaluated before the WHERE statement
-- also be careful when reference below in the WHERE clause
-- Aggregate functions
-- Scalar subqueries
-- Windowing functions 
-- Aliases
select sal as salary, comm as commision 
from emp
where salary < 5000
-- solution:
select * from (
    select sal as salary, comm as commision 
    from emp
) x
where salary < 5000

-- 1.7 concatenate
-- concatenate multiple columns: CLARK WORKS AS MANAGER
-- DB2, Oracle, PostgreSQL
select ename||' WORKS AS A '||job as msg
from emp
where deptno = 10

-- MySQL
select concat(ename, ' WORKS AS A ', job) as msg
from emp
where deptno = 10

-- SQL Server
select ename + ' WORKS AS A ' + job as msg
from emp
where deptno = 10

-- 1.8 Conditional Logic 
-- ELSE is optional 
select ename, sal,
    case when sal <= 2000 then 'UNDERPAID'
         when sal >= 4000 then 'OVERPAID'
         else 'OK'
    end as status
from emp

-- 1.9 limit
-- MySQL and PostgreSQL
select *
from emp limit 5
-- Oracle
-- values from Oracle’s ROWNUM are assigned after each row is fetched
-- ROWNUM = 5 does not work
select * 
from emp
where rownum <= 5 
-- SQL Server
select top 5 *
from emp

-- 1.10 return n random records from a table rand()
-- MySQL
select ename, job
from emp
order by rand() limit 5
-- PostgreSQL
select ename, job
from emp
order by random() limit 5
-- Oracle: dbms_random
-- SQL Server: newid()

-- 1.11 find null values
-- cannot use = or != for testing whether a column is NULL. To determine whether a row has NULL values, you must use IS NULL. 
select *
from emp   
where comm is null

-- 1.12 transform nulls into real values
-- Use the function COALESCE to substitute real values for nulls
-- if null then replace it with 0
select coalesce(comm, 0) 
from emp
-- alternative solution using case when
select 
case when comm is null then comm else 0 end
from emp

-- 1.13 search for patterns
-- return rows that match a particular substring or pattern
select ename, job
from emp
where deptno in (10, 20)
-- Of the employees in departments 10 and 20, you want to return only those that have either an “I” somewhere in their name or a job title ending with “ER”
-- the percent (%) operator matches any sequence of characters.
select ename, job
from emp
where deptno in (10, 20)
and (ename like '%I%' or job like '%ER')


















