-- Chapter 3: Working with Multiple Tables
-- 3.1 
-- Union all: will include duplicates if they exist
-- Union: will filter out duplicates
select ename as ename_and_dname, deptno
from emp
where deptno = 10
    union all
select '--------', null
from t1
    union all
select dname, deptno
from dept

-- 3.2 combine related rows
-- join
select e.ename, d.loc
from emp e, dept d   /* inner-join */ 
where e.deptno = d.deptno
and e.deptno = 10
-- same as:
select e.ename, d.loc
from emp e inner join dept d  
on (e.deptno = d.deptno)
where e.deptno = 10

-- 3.3 find rows in common between two tables
-- find common rows between two tables
-- Join the tables on all the columns necessary
-- or using INTERSECT to return intersection (common rows) of the two tables
-- MySQL and SQL Server
select e.empno,e.ename,e.job,e.sal,e.deptno
from emp e, V
where e.ename = v.ename and e.job = v.job and e.sal = v.sal
-- same as:
select e.empno,e.ename,e.job,e.sal,e.deptno
from emp a join V
on (e.ename = v.ename and e.job = v.job and e.sal = v.sal)
-- If you do not actually need to return columns from view V, you may use the set operation INTERSECT along with an IN predicate
-- INTERSECT will return rows common to both row sources, duplicate rows will not be returned
select empno, ename, job, sal, deptno
from emp
where (ename, job, sal) in (
    select ename, job, sal from emp 
    intersect
    select ename, job, sal from V)

-- 3.4 retrive values from one table that do not exist in another (**)
-- exist in dept but not emp
-- DB2, PostgreSQL, and SQL Server
-- Set difference functions: EXCEPT - takes the first result set and removes from it all rows found in the second result set, will not return duplicates 
select deptno from dept
except 
select deptno from emp
-- Oracle
select deptno from dept 
minus
select deptno from emp
-- MySQL
-- does not remove duplicates
-- In SQL, “TRUE or NULL” is TRUE, but “FALSE or NULL” is NULL! 
-- if Null exists in emp, then not in does not work since Not(False or Null) = Null
select distinct deptno from dept 
where deptno not in (
    select deptno from emp)
-- To avoid the problem with NOT IN and NULLs, use a correlated subquery in conjunction with NOT EXISTS
-- The following example is an alterna‐ tive solution that will not be affected by NULL rows 
select d.deptno
from dept d
where not exists (
    select 1 from emp e
    where d.deptno = e.deptno
)

-- 3.5 retrieve rows from one table that do not correspond to rows in another
-- you want to find which departments have no employees
-- DB2, MySQL, PostgreSQL, and SQL Server
select d.*
from dept d left join emp e
on d.deptno = e.deptno
where e.deptno is null

-- 3.6 add joins to a query without interfere with other joins
-- DB2, MySQL, PostgreSQL, and SQL server
select e.ename, d.loc, ed.received
from emp e join dept d
on (e.deptno = d.deptno)
left join emp_bonus eb 
on (e.empno = eb.empno)
order by 2
-- same as:
select e.ename, d.loc, (
       select eb.received from emp_bonus eb
       where eb.empno = e.empno) as received /* only for single value */
from emp e, dept d 
where e.deptno = d.deptno
order by 2

-- 3.7 determine whether two tables have the same data









