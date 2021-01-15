-- Chapter 3: Working with Multiple Tables - Join

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
-- The following example is an alternative solution that will not be affected by NULL rows 
select d.deptno
from dept d
where not exists (
    select 1 from emp e
    where d.deptno = e.deptno
)

-- 3.5 retrieve rows from one table that do not correspond to rows in another (**)
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

-- 3.7 determine whether two tables have the same data (**)
-- find the difference between view V and table EMP combined with the difference between table EMP and view V
-- DB2, PostgreSQL, and SQL Server
(
select empno,ename,job,mgr,hiredate,sal,comm,deptno,
       count(*) as cnt 
from v 
group by empno,ename,job,mgr,hiredate,sal,comm,deptno
except
select empno,ename,job,mgr,hiredate,sal,comm,deptno,
       count(*) as cnt 
from emp  
group by empno,ename,job,mgr,hiredate,sal,comm,deptno
)
union all 
(
select empno,ename,job,mgr,hiredate,sal,comm,deptno,
       count(*) as cnt 
from emp  
group by empno,ename,job,mgr,hiredate,sal,comm,deptno
except
select empno,ename,job,mgr,hiredate,sal,comm,deptno,
       count(*) as cnt 
from v
group by empno,ename,job,mgr,hiredate,sal,comm,deptno
)
-- MySQL and SQL Server
select * from (
    select e.empno,e.ename,e.job,e.mgr,e.hiredate,e.sal,e.comm,e.deptno,
           count(*) as cnt 
    from emp e
    group by empno,ename,job,mgr,hiredate,sal,comm,deptno) e

where not exists (

select null from (
    select v.empno,v.ename,v.job,v.mgr,v.hiredate,v.sal,v.comm,v.deptno,
           count(*) as cnt 
    from v
    group by empno,ename,job,mgr,hiredate,sal,comm,deptno) v
where v.empno = e.empno and 
      v.ename = e.ename and 
      v.job = e.job and 
      coalesce(v.mgr, 0) = coalesce(e.mgr, 0) and 
      v.hiredate = e.hiredate and 
      v.sal = e.sal and 
      coalesce(v.comm, 0) = coalesce(e.comm, 0) and 
      v.deptno = e.deptno and 
      v.cnt = e.cnt
)
union all
select * from (
    select v.empno,v.ename,v.job,v.mgr,v.hiredate,v.sal,v.comm,v.deptno,
           count(*) as cnt 
    from v
    group by empno,ename,job,mgr,hiredate,sal,comm,deptno) v

where not exists (

select null from (   
    select e.empno,e.ename,e.job,e.mgr,e.hiredate,e.sal,e.comm,e.deptno,
           count(*) as cnt 
    from emp e
    group by empno,ename,job,mgr,hiredate,sal,comm,deptno) e
where v.empno = e.empno and 
      v.ename = e.ename and 
      v.job = e.job and 
      coalesce(v.mgr, 0) = coalesce(e.mgr, 0) and 
      v.hiredate = e.hiredate and 
      v.sal = e.sal and 
      coalesce(v.comm, 0) = coalesce(e.comm, 0) and 
      v.deptno = e.deptno and 
      v.cnt = e.cnt
)

-- 3.8 identify and avoid cartesian products
select e.ename, d.loc
from emp e, dept d 
where e.deptno = 10
and e.deptno = d.deptno

-- 3.9 perform joins when using aggregates
-- compute total salary and bonus for department 10
-- same person gets multiple bonus
/*
Typically when duplicates are returned due to a join, you can avoid miscalculations by aggregate functions in two ways: you can simply use the keyword DISTINCT in the call to the aggregate function, so only unique instances of each value are used in the computation; or you can perform the aggregation first prior to joining
*/
-- Works for all DBMSs
select deptno, 
       sum(distinct sal) as total_sal, -- remove duplicates
       sum(bonus) as total_bonus
from (
    select e.empno,
           e.ename,
           e.sal,
           e.deptno,
           e.sal* case when eb.type = 1 then .1
                       when eb.type = 2 then .2
                       else .3
                    end as bonus
    from emp e, emp_bonus eb
    where a.empno = eb.empno
    and e.deptno = 10
    ) x
group by deptno
-- DB2, Oracle, and SQL Server
-- sum over without group by
select distinct deptno, total_sal, total_bonus
from (
    select e.empno,
           e.ename,
           sum(distinct e.sal) over (partition by e.deptno) as total_sal,
           e.deptno,
           sum(e.sal* case when eb.type = 1 then .1
                       when eb.type = 2 then .2
                       else .3 end) over (partition by e.deptno) as total_bonus
    from emp e, emp_bonus eb
    where e.empno = eb.empno
    and e.deptno = 10
    ) x

-- what if some employees have same salary?
-- The following query is an alternative solution—necessary if there could be duplicate values in the column you are summing
-- sum salary first then sum bonus to remove duplicates when calculating salary
-- Works for all DBMSs
select d.deptno,
       d.total_sal,
       sum(e.sal*case when eb.type = 1 then .1
                      when eb.type = 2 then .2
                      else .3 end) as total_bonus
from emp e,
     emp_bonus eb,
     (
      select deptno, sum(sal) as total_sal from emp 
      where deptno = 10 
      group by deptno
     ) d
where e.deptno = d.deptno and e.empno = eb.empno
group by d.deptno, d.total_sal

-- 3.10 perform outer joins when using aggregates
-- not all employees in department 10 have been given bonuses
-- DB2, MySQL, PostgreSQL, and SQL Server
select deptno, 
       sum(distinct sal) as total_sal, -- remove duplicates
       sum(bonus) as total_bonus
from (
    select e.empno,
           e.ename,
           e.sal,
           e.deptno,
           e.sal* case when eb.type is null then 0  -- modified
                       when eb.type = 1 then .1
                       when eb.type = 2 then .2
                       else .3 end as bonus
    from emp e left outer join emp_bonus eb
    on (a.empno = eb.empno)
    where e.deptno = 10
    ) x
group by deptno

-- 2
select d.deptno,
       d.total_sal,
       sum(e.sal*case when eb.type is null then 0
                      when eb.type = 1 then .1
                      when eb.type = 2 then .2
                      else .3 end) as total_bonus
from emp e,
     emp_bonus eb,
     (
      select deptno, sum(sal) as total_sal from emp 
      where deptno = 10 
      group by deptno
     ) d
where e.deptno = d.deptno and e.empno = eb.empno
group by d.deptno, d.total_sal

-- 3.11 return missing data from multiple tables
-- Use a full outer join to return missing data from both tables based on a common value
-- DB2, PostgreSQL, and SQL Server
select d.deptno,d.dname,e.ename
from dept d full outer join emp e 
on (d.deptno=e.deptno)
-- MySQL does not have full join. Use union instead
select d.deptno,d.dname,e.ename
from dept d right outer join emp e
on (d.deptno=e.deptno)
union   /*  remove duplicates */
select d.deptno,d.dname,e.ename
from dept d left outer join emp e
on (d.deptno=e.deptno)

-- 3.12 use nulls in operations and comparisons
-- find all employees in EMP whose commission (COMM) is less than the commission of employee WARD. Employees with a NULL commission should be included as well
select ename, comm
from emp 
where coalesce(comm, 0) < (select comm from emp where ename = 'WARD')











