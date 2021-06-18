-- Chapter 6: Working with Strings

-- 6.1 walking a string (**)
-- traverse a string to return each character as a row
-- use a cartesian product to generate the number of rows needed to return each character of a string on its own line
-- Then use substr to extract the characters 
/* 
The key to iterating through a string’s characters is to join against a table that has enough rows to produce the required number of iterations.
*/
select substr(e.ename, iter.pos, 1) as C 
from (select ename from emp where ename = 'KING') e,
     (select id as pos from t10) iter
where iter.pos <= length(e.ename)
-- walking E.ENAME and exposing different portions (more than a single character) of the string
select substr(e.ename, iter.pos) a,
       substr(e.ename, length(e.ename)-iter.pos+1) b
from (select ename from emp where ename = 'KING') e,
     (select id pos from t10) iter
where iter.pos <= length(e.ename)

/*
     A         B
--------------------
    KING       G
    ING        NG
    NG         ING
    G          KING
*/
-- 6.2 embedding quotes within string literals (using two quotes inside)
select 'g''day mate'  qmarks from t1 union all
select 'beavers'' teeth'     from t1 union all
select ''''                  from t1 

/*
QMARKS 
-------------- 
g'day mate 
beavers' teeth
'
*/

select 'apples core', 'apple''s core',
       case when '' is null then 0 else 1 end as mark
from t1

/*
'APPLESCORE  'APPLE''SCOR   mark
--------------------------------
apples core  apple's core   0

*/

-- 6.3 count the occurrences of a character in a string (**)
-- count the number of times a character or substring occurs within a given string
-- count how many commas are in the string
-- Subtract the length of the string without the commas from the original length of the string to determine the number of commas in the string
# count the number of comma
select (length('10,CLARK,MANAGER')-length(replace('10,CLARK,MANAGER', ',', '')))/length(',') as cnt 
from t1

select (length('HELLO HELLO')-length(replace('HELLO HELLO', 'LL', '')))/length('LL') as correct_cnt,
        length('HELLO HELLO')-length(replace('HELLO HELLO', 'LL', '')) as incorrect_cnt
from t1

-- 6.4 remove unwanted characters from a string (**)
-- remove vowels from names and remove 0 from sal
-- PostgreSQL and SQL Server
select ename,
    replace(translate(ename, 'aaaaa', 'AEIOU'), 'a', '') as stripped1,
    sal,
    replace(cast(sal as char(4)), '0', '') as stripped2
from emp

-- MySQL
select ename, 
   regexp_replace(ename, '[AEIOU]', '') ename2,
   sal,
   replace(sal, 0, '') sal2
from emp

-- 6.5 separate numeric and character data (**)
-- data: SMITH800
-- PostgreSQL
-- [[:alpha:]] matches any alphabets
-- '' is the replacement string
-- 'g' instructs the function to remove all alphabets, not just the first one.
SELECT regexp_replace('ABC12345xyz','[[:alpha:]]','','g');
-- output '12345'
SELECT regexp_replace('ABC12345xyz','[[:digit:]]','','g');
-- output 'ABCxyz'
select  regexp_replace(data, '[[:digit:]]', '', 'g') as ename
        regexp_replace(data, '[[:alpha:]]', '', 'g') as sal
from (select ename||sal as data from emp) x

-- MySQL
select data,
       regexp_replace(data, '[A-Z]', '') as sal, 
       regexp_replace(data, '[0-9]', '') as name 
from (select concat(ename,sal) as data from emp) a;

-- 6.6 determine whether a string is alphanumeric
-- return ALLEN30, WARD30..
-- convert all alphanumeric characters to a single character or ""
-- remove those no empty, which means data has other characters other than [A-Z0-9]

create view V as 
    select ename as data 
    from emp
    where deptno = 10
    union all
    select concat(ename, ',$', sal, '.00') as data
    from emp
    where deptno = 20
    union all 
    select concat(ename, deptno) as data
    from emp
    where deptno = 30
    ;

# return data with no other characters except [0-9A-Za-z]
select data from V  where data regexp '[^0-9A-Za-z]' = 0;

-- 6.7 extract initials from a name (**)
-- MySQL
-- CONCAT_WS(separator, expression1, expression2, expression3,...)
-- The SUBSTRING_INDEX() function returns a substring of a string before a specified number of delimiter occurs.
-- SUBSTRING_INDEX(string, delimiter, number)
-- SELECT SUBSTRING_INDEX("www.w3schools.com", ".", 1); => www
-- SELECT SUBSTRING_INDEX("www.w3schools.com", ".", 2); => www.w3schools

-- TRIM() function returns a string after removing all prefixes or suffixes from the given string.
-- SELECT TRIM(LEADING 'leading' FROM 'leadingtext' );     => text
-- SELECT TRIM(TRAILING 'trailing' FROM 'texttrailing' );  => text
-- SELECT TRIM(BOTH 'leadtrail' FROM 'leadtrailtextleadtrail'); => text

select concat_ws('.', "S", "G", "W") as initials;
select substring_index('Stewie Griffin Western', ' ', 1) as first_name,  # Stewie
       substring_index('Stewie Griffin Western', ' ', -1) as last_name;  # Western  

select case when cnt = 2 then
    concat_ws('.', 
         substr(substring_index(name, ' ', 1),1,1),  # S
         substr(name, length(substring_index(name, ' ', 1))+2,1),   # G
         substr(substring_index(name, ' ', -1),1,1)  # W
         )
    else
    concat_ws('.',
         substr(substring_index(name, ' ', 1),1,1),
         substr(substring_index(name, ' ',-1),1,1)
        )
    end as initials
from (
    select name, length(name)-length(replace(name, ' ','')) as cnt # finds the number of white spaces in the name
    from (
        select replace('Stewie Griffin Western', '.','') as name # remove any periods in the name
    ) y
) x
-- >> S.G.W 

-- 6.8 order by parts of a string
-- order your result set based on a substring
-- order by the last two characters of each name
-- MySQL
select ename from emp order by substr(ename, -2);

-- 6.9 order by a number in a string     
-- data: SMITH 7369 RESEARCH 
create view V2 as 
    select concat(e.ename, ' ',
           e.empno, ' ',                 # cast(e.empno as char(4))
           d.dname) as data 
    from emp e, dept d
    where e.deptno = d.deptno

select data, regexp_replace(data, '[^0-9]', '') as num
from V2 order by 2;

drop view V2;

-- 6.10 create a delimited list from table rows (**)
/*
10 CLARK
10 KING
10 MILLER

=> 10 CLARK,KING,MILLER
*/
-- MySQL
-- Group_concat
select deptno, group_concat(ename order by empno separator ',') as emps
from emp
group by deptno

-- PostgreSQL and SQL Server
select deptno,
string_agg(ename order by empno separator ',') as emps
from emp
group by deptno

-- 6.11 convert delimited data into a multivalued in-list (**)
-- walk the string
/* following command only return 1 record in MySQL
select ename,sal,deptno
from emp
where empno in ( '7654,7698,7782,7788' )
*/
-- SQL
-- by walking the string passed to the IN-list, convert it to rows:
-- select substring_index('7654,2,45,6', ',', 1) as test;
-- => 7654
-- select substring_index('7654,2,45,6', ',', 2) as test;
-- => 7654,2
select empno, ename, sal, deptno
from emp
where empno in (
    select substring_index(substring_index(list.vals,',',iter.pos),',',-1) empno
    from (select id as pos from t10) as iter,
         (select '7654,7698,7782,7788' as vals) as list
    where iter.pos <= (length(list.vals)-length(replace(list.vals, ',',''))) + 1 #4
    );
-- output:
# | empno | ename  | sal  | deptno |
# |  7654 | MARTIN | 1250 |     30 |
# |  7698 | BLAKE  | 2850 |     30 |
# |  7782 | CLARK  | 2450 |     10 |
# |  7788 | SCOTT  | 3000 |     20 |

-- PostgreSQL
-- split_part(data, delim, pos)
-- The function SPLIT_PART does the work of parsing the string. It looks for the value that comes before the nth occurrence of the delimiter. That's why we need to add ',' in the end
select ename,sal,deptno
from emp
where empno in (
    select cast(empno as integer) as empno
    from (
        select split_part(list.vals,',',iter.pos) as empno 
        from (select id as pos from t10) iter,
             (select ','||'7654,7698,7782,7788'||',' as vals from t1) list
        where iter.pos <= length(list.vals)-length(replace(list.vals,',','')) # 5
         )
    where length(empno) > 0
)

-- 6.12 alphabetize a string (order by character)
-- ADAMS => AADMS
-- MySQL
-- group_concat() concatenate the characters in an order
select ename, group_concat(c order by c separator '') as ordered_name
from (
    select ename, substr(a.ename, iter.pos, 1) c 
    from (select id as pos from t10) as iter,
          emp as a
    where iter.pos <= length(a.ename)
    ) x 
group by ename

-- PostgreSQL
select ename, string_agg(c, order by c separator '') as ordered 
from (
    select ename, substr(a.ename, iter.pos, 1) as c
    from emp as a,
         (select id as pos from t10) as iter 
    where iter.pos <= length(a.ename)
    ) x
group by ename

-- 6.13 identify strings that can be treated as numbers
-- return only numeric values from strings
create view V as
    select replace(mixed, ' ','') as mixed
    from (
    select concat(substr(ename,1,2), deptno, substr(ename,3,2)) as mixed
    from emp
    where deptno = 10
    union all
    select empno as mixed
    from emp
    where deptno = 20
    union all
    select ename as mixed
    from emp 
    where deptno = 30
    ) x

-- MySQL
select regexp_replace(mixed, '[^0-9]', "") as num from V where regexp_replace(mixed, '[^0-9]', "") != 0;

-- method2: walk a string and only keep the numbers then group_concat
select v.mixed, iter.pos, substr(v.mixed, iter.pos, 1) as c 
from V as v,
     (select id as pos from t10) as iter 
where iter.pos <= length(v.mixed)
and ascii(substr(v.mixed, iter.pos, 1)) between 48 and 57  # only keep when c is a number
order by 1,2

# cast as a number
select mixed,cast(group_concat(c order by pos separator '') as unsigned) as num
from (
    select v.mixed, iter.pos, substr(v.mixed, iter.pos, 1) as c 
    from V as v,
         (select id as pos from t10) as iter 
    where iter.pos <= length(v.mixed)
    and ascii(substr(v.mixed, iter.pos, 1)) between 48 and 57  # only keep when c is a number
    order by 1,2 
    ) x
group by 1

-- 6.14 extract the nth delimited substring (**)
create view V2 as 
    select 'mo,larry,curly' as name 
    union all 
    select 'tina,gina,jaunita,regina,leena' as name 
    ;

-- pick up the second name 
-- MySQL
select substring_index(substring_index(name, ',', 2),',',-1) as second
from V2;

select name from (
    select iter.pos,
           substring_index(substring_index(src.name, ',', iter.pos), ',', -1) as name
    from V2 as src,
         (select id as pos from t10) as iter  
    where iter.pos <= length(src.name) - length(replace(src.name, ',', '')) + 1 
    ) x
where pos = 2

-- postgreSQL
select name
    from (
    select iter.pos, split_part(src.name,',',iter.pos) as name 
    from (select id as pos from t10) iter,
         (select cast(name as text) as name from v) src 
    where iter.pos <= length(src.name)-length(replace(src.name,',',''))+1 
    )x
where pos = 2

-- 6.15 parse an IP address
-- ip: 111.22.3.4 =>  111  22  3  4
-- MySQL
select substring_index(substring_index("111.22.3.4", '.', iter.pos), '.', -1) as part1

from (select id as pos from t10) as iter
where pos <= length("111.22.3.4") - length(replace("111.22.3.4", '.', ''))+1;

select distinct
       substring_index(substring_index("111.22.3.4", '.', 1), '.', -1) as a,
       substring_index(substring_index("111.22.3.4", '.', 2), '.', -1) as b,
       substring_index(substring_index("111.22.3.4", '.', 3), '.', -1) as c,
       substring_index(substring_index("111.22.3.4", '.', 4), '.', -1) as d

from (select id as pos from t10) as iter
where pos <= length("111.22.3.4") - length(replace("111.22.3.4", '.', ''))+1;

-- 6.16 compare strings by sound
-- identify names with plausible phonetic matches for other names on the list
create table anames (name varchar(15));
insert into anames
values("Johnson"),
      ("Jonson"), 
      ("Jonsen"),
      ("Johnsen"),
      ("Shakespeare"),
      ("Shakspear"),
      ("Shaekspir"),
      ("Shakespar");

select a1.name as e1, a2.name as e2, soundex(a1.name) as e3
from anames as a1 
join anames as a2 
on soundex(a1.name) = soundex(a2.name)
where a1.name != a2.name
order by 1,2

-- 6.17 find text not matching a pattern (**)
-- (237) 438-3333 and 989-387-4321 have two different separator characters
/*
1. Find a way to describe the universe of apparent phone numbers that you want to consider.
2. Remove any validly formatted phone numbers from consideration.
3. See whether you still have any apparent phone numbers left. If you do, you know those are invalidly formatted.
*/

-- define a pattern A: [0-9]{3}[-. ][0-9]{3}[-. ][0-9]{4} 
-- Pattern A checks for two groups of three digits followed by one group of four digits. Any one of a dash (-), a period (.), or a space is accepted as a delimiter between groups.
-- define a well-formated pattern B: [0-9]{3}[-. ][0-9]{3}\1[0-9]{4} 
-- The pattern B uses \1 to reference the first subexpression. Whichever character is matched by ([-. ]) must also be matched by \1
-- replace the well-formated phone numbers with strings of three (*):
-- regexp_replace(texts, '[0-9]{3}[-. ][0-9]{3}\1[0-9]{4}', '***')
-- See whether you still have any apparent phone numbers left

create table employee_comment (emp_id int, texts text);
insert into employee_comment
    values (7369, "126 Varnum, Edmore MI 48829, 989 313-5351"),
           (7499, "1105 McConnell Court
                   Cedar Lake MI 48812
                   Home: 989-387-4321
                   Cell: (237) 438-3333");

select regexp_replace(texts, '[0-9]{3}[-. ][0-9]{3}[-. ][0-9]{4}', '***') as test 
from employee_comment;

-- \1 does not work here!
select emp_id, texts
from employee_comment
where regexp_like(texts, '[0-9]{3}[-. ][0-9]{3}[-. ][0-9]{4}')  # texts have phone number
and   regexp_like(regexp_replace(texts, '[0-9]{3}([-. ])[0-9]{3}\1[0-9]{4}', '***'), '[0-9]{3}[-. ][0-9]{3}[-. ][0-9]{4}')

-- output => 7369 | 126 Varnum, Edmore MI 48829, 989 313-5351 (two differnt separator in phone number)
























