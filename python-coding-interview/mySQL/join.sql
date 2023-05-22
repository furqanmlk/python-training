 select order_id, customer_id, order_date, status 
 from orders;
 /*
+----------+-------------+------------+--------+
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
+----------+-------------+------------+--------+
*/

select customer_id, first_name, last_name, state, points 
from customers;
/*
+-------------+------------+------------+-------+--------+
| customer_id | first_name | last_name  | state | points |
+-------------+------------+------------+-------+--------+
|           1 | Babara     | MacCaffrey | MA    |   2273 |
|           2 | Ines       | Brushfield | VA    |    947 |
|           3 | Freddi     | Boagey     | CO    |   2967 |
|           4 | Ambur      | Roseburgh  | FL    |    457 |
|           5 | Clemmie    | Betchley   | TX    |   3675 |
|           6 | Elka       | Twiddell   | IL    |   3073 |
|           7 | Ilene      | Dowson     | TN    |   1672 |
|           8 | Thacher    | Naseby     | FL    |    205 |
|           9 | Romola     | Rumgay     | CA    |   1486 |
|          10 | Levy       | Mynett     | GA    |    796 |
+-------------+------------+------------+-------+--------+
*/

-- INNER JOIN / JOIN
SELECT o.order_id, c.first_name, c.last_name 
FROM orders as o 
JOIN customers as c 
ON o.customer_id = c.customer_id;
/*
+----------+------------+------------+
| order_id | first_name | last_name  |
+----------+------------+------------+
|        4 | Ines       | Brushfield |
|        7 | Ines       | Brushfield |
|        5 | Clemmie    | Betchley   |
|        8 | Clemmie    | Betchley   |
|        1 | Elka       | Twiddell   |
|       10 | Elka       | Twiddell   |
|        2 | Ilene      | Dowson     |
|        3 | Thacher    | Naseby     |
|        6 | Levy       | Mynett     |
|        9 | Levy       | Mynett     |
+----------+------------+------------+
*/


SELECT order_id, o.product_id, p.name, o.quantity, o.unit_price 
FROM order_items as o 
JOIN products as p 
ON o.product_id = p.product_id;
/*
+----------+------------+------------------------------+----------+------------+
| order_id | product_id | name                         | quantity | unit_price |
+----------+------------+------------------------------+----------+------------+
|        2 |          1 | Foam Dinner Plate            |        2 |       9.10 |
|        6 |          1 | Foam Dinner Plate            |        4 |       8.65 |
|       10 |          1 | Foam Dinner Plate            |       10 |       6.01 |
|        5 |          2 | Pork - Bacon,back Peameal    |        3 |       9.89 |
|        6 |          2 | Pork - Bacon,back Peameal    |        4 |       3.28 |
|        3 |          3 | Lettuce - Romaine, Heart     |       10 |       9.12 |
|        4 |          3 | Lettuce - Romaine, Heart     |        7 |       6.99 |
|        6 |          3 | Lettuce - Romaine, Heart     |        4 |       7.46 |
|        7 |          3 | Lettuce - Romaine, Heart     |        7 |       9.17 |
|        1 |          4 | Brocolinni - Gaylan, Chinese |        4 |       3.74 |
|        2 |          4 | Brocolinni - Gaylan, Chinese |        4 |       1.66 |
|        6 |          5 | Sauce - Ranch Dressing       |        1 |       3.45 |
|        8 |          5 | Sauce - Ranch Dressing       |        2 |       6.94 |
|        2 |          6 | Petit Baguette               |        2 |       2.94 |
|        9 |          6 | Petit Baguette               |        5 |       7.28 |
|        8 |          8 | Island Oasis - Raspberry     |        2 |       8.59 |
|       10 |          9 | Longan                       |        9 |       4.28 |
|        4 |         10 | Broom - Push                 |        7 |       6.40 |
+----------+------------+------------------------------+----------+------------+
*/

