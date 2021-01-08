-- Chapter 5: Metadata Queries
-- 5.1 list tables in a schema
-- PostgreSQL, MySQL, and SQL Server
select table_name
from information_scheme.tables
where table_schema = 'SMEAGOL'

-- 5.2 list a table's columns
-- PostgreSQL, MySQL, and SQL Server
-- Additional useful items of information include length, nullability, and default values
select column_name, data_type, ordinal_position
from information_scheme.columns
where table_schema = 'SMEAGOL'
and table_name = 'EMP'

-- list indexed columns for a table
-- You want list indexes, their columns, and the column position (if available) in the index for a given table
-- PostgreSQL
select a.tablename, a.indexname, b.column_name,
from pg_catalog.pg_indexes a,
     information_scheme.columns b
where a.schemaname = 'SMEAGOL'
and a.tablename = b.tablename
-- MySQL
show index from emp 

-- list constraints on a table
-- list the constraints defined for a table in some schema
-- PostgreSQL, MySQL, and SQL Server
select a.table_name,
       a.constraint_name,
       b.column_name,
       a.constraint_type
from information_scheme.table_constraints a,
     information_scheme.key_column_usage b
where a.table_name = 'EMP'
and   a.table_schema = 'SMEAGOL'
and   a.table_name   = b.table_name
and   a.table_schema = b.table_schema
and   a.constraint_name = b.constraint_name

-- list foreign keys without corresponding indexes
-- PostgreSQL
select
fkeys.table_name, fkeys.constraint_name, fkeys.column_name, ind_cols.indexname
from (
    select
    a.constraint_schema,
    a.table_name,
    a.constraint_name,
    a.column_name 
    from information_schema.key_column_usage a, 
         information_schema.referential_constraints b 
    where a.constraint_name = b.constraint_name 
    and   a.constraint_schema = b.constraint_schema 
    and   a.constraint_schema = 'SMEAGOL' 
    and   a.table_name = 'EMP'
    ) fkeys
    left join
    (
    select 
    a.schemaname, 
    a.tablename, 
    a.indexname, 
    b.column_name 
    from pg_catalog.pg_indexes a,
         information_schema.columns b
    where a.tablename = b.table_name
    and a.schemaname = b.table_schema 
    ) ind_cols
    on (
        fkeys.constraint_schema = ind_cols.schemaname
        and fkeys.table_name    = ind_cols.tablename
        and fkeys.column_name   = ind_cols.column_name)
    where ind_cols.indexname is null 

-- MySQL
show index from emp
/*
compare the output with that of INFORMATION_SCHEMA.KEY_ COLUMN_USAGE.COLUMN_NAME for the same table. If the COLUMN_NAME is listed in KEY_COLUMN_USAGE but is not returned by SHOW INDEX, you know that column is not indexed.
*/

-- use SQL to generate SQL
/*
You want to create dynamic SQL statements, perhaps to automate maintenance tasks. You want to accomplish three tasks in particular: count the number of rows in your tables, disable foreign key constraints defined on your tables, and generate insert scripts from the data in your tables.
*/
-- generate SQL to count all the rows in all your tables;
select 'select count(*) from '||table_name||';' cnts from user_tables;

-- disable foreign keys from all tables
select 'alter table '||table_name||' disable constraints '||constraint_name||';' cons 
from user_constraints
where constraint_type = 'R';

-- generate an insert script from some columns in table EMP
select 'insert into emp(empno, ename, hiredate) '||chr(10)||' values('||empno||', '||''''||ename||''',to_date('||''''||hiredate||''') );' inserts 
from emp
where deptno = 10;
-- i.e. insert into emp(empno,ename,hiredate) 
--      values( 7782,'CLARK',to_date('09-JUN-2006 00:00:00') );

-- 5.7 describe the data dictionary views in an oracle database
select table_name, comments from dictionary
order by table_name

select column_name, comments from dict_columns
where table_name = 'ALL_TAB_COLUMNS'











