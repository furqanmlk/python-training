----------- RegExp ---------------

-- where last_name regexp 'field' -- any where in last name
select * from customers where last_name regexp 'field';
/*
+-------------+------------+------------+------------+--------------+------------------------+---------+-------+--------+
| customer_id | first_name | last_name  | birth_date | phone        | address                | city    | state | points |
+-------------+------------+------------+------------+--------------+------------------------+---------+-------+--------+
|           2 | Ines       | Brushfield | 1986-04-13 | 804-427-9456 | 14187 Commercial Trail | Hampton | VA    |    947 |
+-------------+------------+------------+------------+--------------+------------------------+---------+-------+--------+
*/

-- where last_name regexp '^mac'  -- last_name must starts with mac
 SELECT * FROM customers WHERE last_name REGEXP '^MAC';
 /*
+-------------+------------+------------+------------+--------------+----------------+---------+-------+--------+
| customer_id | first_name | last_name  | birth_date | phone        | address        | city    | state | points |
+-------------+------------+------------+------------+--------------+----------------+---------+-------+--------+
|           1 | Babara     | MacCaffrey | 1986-03-28 | 781-932-9754 | 0 Sage Terrace | Waltham | MA    |   2273 |
+-------------+------------+------------+------------+--------------+----------------+---------+-------+--------+
*/

-- where last_name regexp 'dell$' -- last_name must ends with dell
SELECT * FROM customers WHERE last_name REGEXP 'dell$';
/*
+-------------+------------+-----------+------------+--------------+----------------+---------+-------+--------+
| customer_id | first_name | last_name | birth_date | phone        | address        | city    | state | points |
+-------------+------------+-----------+------------+--------------+----------------+---------+-------+--------+
|           6 | Elka       | Twiddell  | 1991-09-04 | 312-480-8498 | 7 Manley Drive | Chicago | IL    |   3073 |
+-------------+------------+-----------+------------+--------------+----------------+---------+-------+--------+
*/


-- where last_name regexp 'field|mac|rose' -- last_name either contains field or mac or rose
SELECT * FROM customers WHERE last_name 
REGEXP 'field|mac|rose';
/*
+-------------+------------+------------+------------+--------------+------------------------+---------+-------+--------+
| customer_id | first_name | last_name  | birth_date | phone        | address                | city    | state | points |
+-------------+------------+------------+------------+--------------+------------------------+---------+-------+--------+
|           1 | Babara     | MacCaffrey | 1986-03-28 | 781-932-9754 | 0 Sage Terrace         | Waltham | MA    |   2273 |
|           2 | Ines       | Brushfield | 1986-04-13 | 804-427-9456 | 14187 Commercial Trail | Hampton | VA    |    947 |
|           4 | Ambur      | Roseburgh  | 1974-04-14 | 407-231-8017 | 30 Arapahoe Terrace    | Orlando | FL    |    457 |
+-------------+------------+------------+------------+--------------+------------------------+---------+-------+--------+
*/

-- where last_name regexp 'dell$|^mac|rush' -- last_name either ends with dell or starts with mac or contains rush
SELECT * FROM customers WHERE last_name REGEXP 'dell$|^mac|rush';
/*
+-------------+------------+------------+------------+--------------+------------------------+---------+-------+--------+
| customer_id | first_name | last_name  | birth_date | phone        | address                | city    | state | points |
+-------------+------------+------------+------------+--------------+------------------------+---------+-------+--------+
|           1 | Babara     | MacCaffrey | 1986-03-28 | 781-932-9754 | 0 Sage Terrace         | Waltham | MA    |   2273 |
|           2 | Ines       | Brushfield | 1986-04-13 | 804-427-9456 | 14187 Commercial Trail | Hampton | VA    |    947 |
|           6 | Elka       | Twiddell   | 1991-09-04 | 312-480-8498 | 7 Manley Drive         | Chicago | IL    |   3073 |
+-------------+------------+------------+------------+--------------+------------------------+---------+-------+--------+
*/

-- where last_name regexp '[gim]e' -- last_name contains either 'ge' or 'ie' or 'me'
SELECT * FROM customers WHERE last_name REGEXP '[gim]e';
/*
+-------------+------------+------------+------------+--------------+------------------------+------------------+-------+--------+
| customer_id | first_name | last_name  | birth_date | phone        | address                | city             | state | points |
+-------------+------------+------------+------------+--------------+------------------------+------------------+-------+--------+
|           2 | Ines       | Brushfield | 1986-04-13 | 804-427-9456 | 14187 Commercial Trail | Hampton          | VA    |    947 |
|           3 | Freddi     | Boagey     | 1985-02-07 | 719-724-7869 | 251 Springs Junction   | Colorado Springs | CO    |   2967 |
+-------------+------------+------------+------------+--------------+------------------------+------------------+-------+--------+
*/

-- where last_name regexp '[a-h]e' -- last_name contains either ae, or be or ce or de or ... he
 SELECT * FROM customers WHERE last_name REGEXP '[a-h]e';
 /*
+-------------+------------+-----------+------------+--------------+----------------------+------------------+-------+--------+
| customer_id | first_name | last_name | birth_date | phone        | address              | city             | state | points |
+-------------+------------+-----------+------------+--------------+----------------------+------------------+-------+--------+
|           3 | Freddi     | Boagey    | 1985-02-07 | 719-724-7869 | 251 Springs Junction | Colorado Springs | CO    |   2967 |
|           5 | Clemmie    | Betchley  | 1973-11-07 | NULL         | 5 Spohn Circle       | Arlington        | TX    |   3675 |
|           6 | Elka       | Twiddell  | 1991-09-04 | 312-480-8498 | 7 Manley Drive       | Chicago          | IL    |   3073 |
+-------------+------------+-----------+------------+--------------+----------------------+------------------+-------+--------+
*/