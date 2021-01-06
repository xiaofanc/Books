-- Chapter 4: Inserting, Updating, and Deleting
/*
• Inserting new records into your database
• Updating existing records
• Deleting records that you no longer want
*/
-- 4.1 insert a new record
insert into dept (deptno, dname, loc)
values (50, 'PROGRAMMING', 'BALTIMORE')

insert into dept  -- all of the columns
values (50,'PROGRAMMING','BALTIMORE')

/* multi row insert */
insert into dept (deptno, dname, loc)
values (50, 'PROGRAMMING', 'BALTIMORE')
       (30, 'fagaggad', 'dafafaf')

-- 4.2 insert default values
create table D (id integer default 0)
-- works for all 
insert into D values (default)
-- MySQL
insert into D values ()   -- In this case, all columns will be set to their default values
-- PostgreSQL and SQL Server 
insert into D default values

create table D (id integer default 0, foo varchar(10))
insert into D (foo) values ('Bar') /* This statement will result in a row in which ID is 0 and FOO is BAR */

-- 4.3 override a default value with null
create table D (id integer default 0, foo VARCHAR(10))
-- insert a row with a NULL value for ID
insert into D (id, foo)
values (null, 'Brighten')

-- 4.4 copy rows from one table into another
insert into dept_east (deptno,dname,loc)
select deptno,dname,loc
from dept
where loc in ( 'NEW YORK','BOSTON' )

-- 4.5 copy a table definition (**)
-- create a new table having the same set of columns as an existing table
-- Oracle, MySQL, and PostgreSQL
-- Use the CREATE TABLE command with a subquery that returns no rows
create table dept_2 as 
select *
from dept
where 1=0  /* the expression “1 = 0” in the WHERE clause of the query causes no rows to be returned */

-- 4.6 insert into multiple tables at once
-- MySQL, PostgreSQL, and SQL Server does not support 

-- 4.7 block inserts to certain columns
-- you want to allow a program to insert into EMP, but only into the EMPNO, ENAME, and JOB columns
-- Create a view on the table exposing only those columns you want to expose

-- 4.8 modify records in a table
-- increase the salaries of everyone in department 20 by 10%
update emp 
    set sal = sal*1.10
where deptno = 20

-- 4.9 update when corresponding rows exist
-- if an employee appears in table EMP_BONUS, you want to increase that employee’s salary (in table EMP) by 20%
update emp 
    set sal = sal*1.2
where empno in (select empno from emp_bonus)
-- same as:
update emp 
    set sal = sal*1.2
where exists (select null from emp_bonus where emp.empno = emp_bonus.empno)

-- 4.10 update with values from another table (**)
-- NEW_SAL does not have any other departments, so the SAL and COMM for employees in DEPTNOs 20 and 30 are set to NULL?
-- MySQL
update emp e, new_sal ns 
    set e.sal = ns.sal, e.comm = ns.sal/2
where e.deptno = ns.deptno
-- PostgreSQL
update emp 
    set sal = ns.sal, comm = ns.sal/2
from new_sal ns 
where emp.deptno = ns.deptno 

-- 4.11 merge records
-- MySQL does not have a MERGE statement
merge into emp_commission ec 
using (select * from emp) emp
on (ec.empno=emp.empno)
when matched then
    update set ec.comm = 1000
    delete where (sal < 2000)
when not matched then
insert (ec.empno,ec.ename,ec.deptno,ec.comm)
values (emp.empno,emp.ename,emp.deptno,emp.comm)

-- 4.12 delete all records from a table
-- TRUNCATE?
delete from emp

-- 4.13 delete specific records 
delete from emp where deptno = 10

-- 4.14 delete a single record
delete from emp where empno = 7782

-- 4.15 deleting referential integrity violations
-- some employees are assigned to departments that do not exist. You want to delete those employees
delete from emp 
where not exists (
    select * from dept where dept.deptno = emp.deptno)
-- same as:
delete from emp
where deptno not in (select deptno from dept)

-- 4.16 delete duplicate records
-- The key to the solution is that you group by the values that are duplicated
delete from dups
where id not in (
        select min(id) from dups group by name)

-- MySQL: cannot reference the same table twice in a delete
delete from dupes
where id not in (
    select min(id)
    from (select id, name from dupes) tmp
    group by name)

-- 4.17 deleting records referenced from another table (**)
-- delete from EMP the records for those employees working at a department that has three or more accidents
/*
HAVING Clause returns the grouped records which match the given condition
HAVING Clause filter the groups with the specific condition
WHERE Clause cannot be combined with aggregate results
WHERE Clause restricts records before GROUP BY Clause, whereas HAVING Clause restricts groups after GROUP BY Clause are performed.
https://www.datacamp.com/community/tutorials/group-by-having-clause-sql?utm_source=adwords_ppc&utm_campaignid=1565261270&utm_adgroupid=67750485268&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=295208661514&utm_targetid=dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=9031905&gclid=CjwKCAiAudD_BRBXEiwAudakXywk2kjXulDtNgX2dA7g8UzdTaxZ9yDcRdwFpyCLA7Xw1dJ8aLbCcxoCIgEQAvD_BwE
*/
delete from emp
where deptno in (
    select deptno 
    from dept_accidents
    group by deptno
    having count(*) >= 3)



























