
SELECT order_id, customer_id, order_date, status 
FROM orders;

/*+----------+-------------+------------+--------+
| order_id | customer_id | order_date | status |
+----------+-------------+------------+--------+
|        1 |           6 | 2019-01-30 |      1 |
|        2 |           7 | 2018-08-02 |      2 |
|        3 |           8 | 2017-12-01 |      1 |
|        4 |           2 | 2017-01-22 |      1 |
|        5 |           5 | 2017-08-25 |      2 |
|        6 |          10 | 2018-11-18 |      1 |
|        7 |           2 | 2018-09-22 |      2 |
|        8 |           5 | 2018-06-08 |      1 |
|        9 |          10 | 2017-07-05 |      2 |
|       10 |           6 | 2018-04-22 |      2 |
+----------+-------------+------------+--------+*/

 SELECT * 
 FROM order_statuses;

/*+-----------------+-----------+
| order_status_id | name      |
+-----------------+-----------+
|               1 | Processed |
|               2 | Shipped   |
|               3 | Delivered |
+-----------------+-----------+*/

/*
joining three tables orders, order_statuses and customers to display 
+----------+-------------+------------+--------+---------
| order_id | order_date | first_name | last_name | status
+----------+-------------+------------+--------+----------

Relation between ORDERS and CUSTOMERS tables are based on customer_id
Relation between ORDERS and ORDER_STATUSES tables are based on order_id

customer_id --> is common in ORDERS and CUSTOMERS tables
 ---JOIN will be used btw ORDERS and CUSTOMERS
order_date --> is from ORDERS
first_name , last_name -> are from CUSTOMERS 
status --> is common in ORDERS and ORDER_STATUSES
 --- JOIN will be used btw ORDERS and ORDER_STATUSES
 */

 SELECT 
	o.order_id, o.order_date,
    c.first_name, c.last_name,
    os.name as status
FROM orders as o
JOIN customers as c
	 ON o.customer_id = c.customer_id
JOIN order_statuses as os
     ON o.status = os.order_status_id
;

/*
+----------+------------+------------+------------+-----------+
| order_id | order_date | first_name | last_name  | status    |
+----------+------------+------------+------------+-----------+
|        1 | 2019-01-30 | Elka       | Twiddell   | Processed |
|        3 | 2017-12-01 | Thacher    | Naseby     | Processed |
|        4 | 2017-01-22 | Ines       | Brushfield | Processed |
|        6 | 2018-11-18 | Levy       | Mynett     | Processed |
|        8 | 2018-06-08 | Clemmie    | Betchley   | Processed |
|        2 | 2018-08-02 | Ilene      | Dowson     | Shipped   |
|        5 | 2017-08-25 | Clemmie    | Betchley   | Shipped   |
|        7 | 2018-09-22 | Ines       | Brushfield | Shipped   |
|        9 | 2017-07-05 | Levy       | Mynett     | Shipped   |
|       10 | 2018-04-22 | Elka       | Twiddell   | Shipped   |
+----------+------------+------------+------------+-----------+
*/


 SELECT * FROM clients;
/*
+-----------+-------------+--------------------------+---------------+-------+--------------+
| client_id | name        | address                  | city          | state | phone        |
+-----------+-------------+--------------------------+---------------+-------+--------------+
|         1 | Vinte       | 3 Nevada Parkway         | Syracuse      | NY    | 315-252-7305 |
|         2 | Myworks     | 34267 Glendale Parkway   | Huntington    | WV    | 304-659-1170 |
|         3 | Yadel       | 096 Pawling Parkway      | San Francisco | CA    | 415-144-6037 |
|         4 | Kwideo      | 81674 Westerfield Circle | Waco          | TX    | 254-750-0784 |
|         5 | Topiclounge | 0863 Farmco Road         | Portland      | OR    | 971-888-9129 |
+-----------+-------------+--------------------------+---------------+-------+--------------+
*/


SELECT * FROM payments;
/*
+------------+-----------+------------+------------+--------+----------------+
| payment_id | client_id | invoice_id | date       | amount | payment_method |
+------------+-----------+------------+------------+--------+----------------+
|          1 |         5 |          2 | 2019-02-12 |   8.18 |              1 |
|          2 |         1 |          6 | 2019-01-03 |  74.55 |              1 |
|          3 |         3 |         11 | 2019-01-11 |   0.03 |              1 |
|          4 |         5 |         13 | 2019-01-26 |  87.44 |              1 |
|          5 |         3 |         15 | 2019-01-15 |  80.31 |              1 |
|          6 |         3 |         17 | 2019-01-15 |  68.10 |              1 |
|          7 |         5 |         18 | 2019-01-08 |  32.77 |              1 |
|          8 |         5 |         18 | 2019-01-08 |  10.00 |              2 |
+------------+-----------+------------+------------+--------+----------------+
*/

 select * from payment_methods;
/*
+-------------------+---------------+
| payment_method_id | name          |
+-------------------+---------------+
|                 1 | Credit Card   |
|                 2 | Cash          |
|                 3 | PayPal        |
|                 4 | Wire Transfer |
+-------------------+---------------+
*/

/*
Using above three tables, display data like this 
+------------+------------+--------+-------------+----------------+
| date       | invoice_id | amount | client_name | payment_method |
+------------+------------+--------+-------------+----------------+
| 2019-02-12 |          2 |   8.18 | Topiclounge | Credit Card    |
| 2019-01-03 |          6 |  74.55 | Vinte       | Credit Card    |
| 2019-01-11 |         11 |   0.03 | Yadel       | Credit Card    |
| 2019-01-26 |         13 |  87.44 | Topiclounge | Credit Card    |
| 2019-01-15 |         15 |  80.31 | Yadel       | Credit Card    |
| 2019-01-15 |         17 |  68.10 | Yadel       | Credit Card    |
| 2019-01-08 |         18 |  32.77 | Topiclounge | Credit Card    |
| 2019-01-08 |         18 |  10.00 | Topiclounge | Cash           |
+------------+------------+--------+-------------+----------------+
*/

SELECT 
	p.date, p.invoice_id, p.amount,
    c.name as client_name,
    pm.name as payment_method
FROM payments as p
JOIN clients as c
     ON p.client_id = c.client_id
JOIN payment_methods as pm
	ON p.payment_method = pm.payment_method_id
;