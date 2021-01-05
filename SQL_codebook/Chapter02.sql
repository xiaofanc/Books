-- Chapter 2: Sorting Query Results
-- 2.1 order by
select ename. job, sal
from emp
where depno = 10
order by 3 desc -- asc is default

-- 2.2 sort by multiple fields
-- sort the rows from EMP first by DEPTNO ascending, then by salary descending
-- You are generally permitted to order by a column not in the SELECT list
-- if you are using GROUP BY or DISTINCT in your query, you cannot order by columns that are not in the SELECT list
select empno, depto, sal, ename, job
from emp
order by deptno, sal desc

-- 2.3 sort by substring
-- sort by the last two characters in the JOB field
-- DB2, MySQL, Oracle, and PostgreSQL
select ename, job
from emp
order by substr(job, length(job)-1)
-- SQL Server
select ename,job
from emp
order by substring(job,len(job)-1,2)

-- 2.4 sort mixed alphanumeric data (**)
-- You have mixed alphanumeric data and want to sort by either the numeric or character portion of the data
-- data: SMITH 20
/*
Use the functions REPLACE and TRANSLATE to modify the string for sorting
translate '0123456789' to '##########' in data
replace '#' with '' in data
characters were left 
replace characters with '' in data, then nums were left
*/
-- Oracle, SQL Server, and PostgreSQL
-- The TRANSLATE function is not currently supported by MySQL
select data,
replace(translate(data, '0123456789', '##########'),'#','') as chars,
replace(data, 
    replace(translate(data, '0123456789', '##########'),'#',''), '') as nums,
from V

-- 2.5 deal with Nulls when sorting (**)
-- You need a way to specify whether nulls sort last or first
-- you want to sort non-NULL values in ascending or descending order and all NULL values last, you can use a CASE expression to conditionally sort the column
-- DB2, MySQL, PostgreSQL, and SQL Server
/*
Use a CASE expression to “flag” when a value is NULL. The idea is to have a flag with two values: one to represent NULLs, the other to represent non-NULLs. Once you have that, simply add this flag column to the ORDER BY clause. You’ll easily be able to control whether NULL values are sorted first or last without interfering with non-NULL values
*/

/* NON-NULL COMM SORTED ASCENDING, ALL NULLS LAST */
select ename, sal, comm
from (
    select ename, sal, comm, 
           case when comm is null then 0 else 1 end as is_null
    from emp
     ) x
order by is_null desc, comm

/* NON-NULL COMM SORTED DESCENDING, ALL NULLS LAST */
select ename, sal, comm
from (
    select ename, sal, comm, 
           case when comm is null then 0 else 1 end as is_null
    from emp
     ) x
order by is_null desc, comm desc

/* NON-NULL COMM SORTED ASCENDING, ALL NULLS FIRST */
select ename, sal, comm
from (
    select ename, sal, comm, 
           case when comm is null then 0 else 1 end as is_null
    from emp
     ) x
order by is_null, comm

/* NON-NULL COMM SORTED DESCENDING, ALL NULLS FIRST */
select ename, sal, comm
from (
    select ename, sal, comm, 
           case when comm is null then 0 else 1 end as is_null
    from emp
     ) x
order by is_null, comm desc

-- 2.6 sort on a Data-Dependent Key (**)
-- if JOB is SALESMAN, you want to sort on COMM; otherwise, you want to sort by SAL
select ename, sal, job, comm
from emp
order by case when job = 'SALESMAN' then comm else sal end
-- same as:
select ename, sal, job, comm
       case when job = 'SALESMAN' then comm else sal end as ordered
from emp
order by 5






