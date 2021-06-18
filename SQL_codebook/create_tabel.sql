
brew services start mysql
mysql -u root -p 
create user 'XiaofangChu'@'localhost' identified by 'Baby940214!';
grant all privileges on *.* to 'XiaofangChu'@'localhost';
go back to terminal
mysql -u XiaofangChu -p
create database SQL_codebook;
use SQL_codebook;
 
create database SQL_codebook;
use SQL_codebook;
create table emp (empno integer, ename varchar(10), job varchar(15), mgr integer, hiredate date, sal int, comm int, deptno int);
insert into emp
values(7369, "SMITH",  "CLERK",      7902, "2005-12-17",  800,   NULL , 20),
        (7499, "ALLEN",  "SALESMAN",   7698, "2006-02-20",  1600,  300 , 30),
        (7521, "WARD",   "SALESMAN",   7698, "2006-02-22",  1250,  500 , 30),
        (7566, "JONES",  "MANAGER",    7839, "2006-04-02",  2975,  NULL, 20),
        (7654, "MARTIN", "SALESMAN",   7698, "2006-09-28",  1250,  1400, 30),
        (7698, "BLAKE",  "MANAGER",    7839, "2006-05-01",  2850,  NULL, 30),
        (7782, "CLARK",  "MANAGER",    7839, "2006-06-09",  2450,  NULL, 10),
        (7788, "SCOTT",  "ANALYST",    7566, "2007-12-09",  3000,  NULL, 20),
        (7839, "KING",   "PRESIDENT",  NULL, "2006-11-17",  5000,  NULL, 10),
        (7844, "TURNER", "SALESMAN",   7698, "2006-09-08",  1500,  0   , 30),
        (7876, "ADAMS",  "CLERK",      7788, "2008-01-12",  1100,  NULL, 20),
        (7900, "JAMES",  "CLERK",      7698, "2006-12-03",  950,   NULL, 30),
        (7902, "FORD",   "ANALYST",    7566, "2006-12-03",  3000,  NULL, 20),
        (7934, "MILLER", "CLERK",      7782, "2007-01-23",  1300,  NULL, 10);


create table dept (deptno int, dname varchar(20), loc varchar(20));
insert into dept
values(10,        "ACCOUNTING",     "NEW YORK"),
      (20,        "RESEARCH",       "DALLAS"),
      (30,        "SALES",          "CHICAGO"),
      (40,        "OPERATIONS",     "BOSTON");


create table emp_bonus (empno int, received date, type int);
insert into emp_bonus
values
(7934, "2005-03-17", 1),
(7934, "2005-02-15", 2),
(7839, "2005-02-15", 3),
(7782, "2005-02-15", 1);


create table t10 (id int);
insert into t10
values(1),(2),(3),(4),(5),(6),(7),(8),(9),(10);

show tables;

/*
3.7 v

 7369 SMITH  CLERK      7902 17-12-2005  800        20
 7499 ALLEN  SALESMAN   7698 20-02-2006  1600  300  30
 7521 WARD   SALESMAN   7698 22-02-2006  1250  500  30
 7566 JONES  MANAGER    7839 02-04-2006  2975       20
 7654 MARTIN SALESMAN   7698 28-09-2006  1250  1400 30
 7698 BLAKE  MANAGER    7839 01-05-2006  2850       30
 7788 SCOTT  ANALYST    7566 09-12-2007  3000       20
 7844 TURNER SALESMAN   7698 08-09-2006  1500  0    30
 7876 ADAMS  CLERK      7788 12-01-2008  1100       20
 7900 JAMES  CLERK      7698 03-12-2006  950        30
 7902 FORD   ANALYST    7566 03-12-2006  3000       20
 7521 WARD   SALESMAN   7698 22-02-2006  1250  500  30

*/


