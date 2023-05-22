
select * from employees;
/*
+-------------+------------+------------+-----------------------------+--------+------------+-----------+
| employee_id | first_name | last_name  | job_title                   | salary | reports_to | office_id |
+-------------+------------+------------+-----------------------------+--------+------------+-----------+
|       33391 | D'arcy     | Nortunen   | Account Executive           |  62871 |      37270 |         1 |
|       37270 | Yovonnda   | Magrannell | Executive Secretary         |  63996 |       NULL |        10 |
|       37851 | Sayer      | Matterson  | Statistician III            |  98926 |      37270 |         1 |
|       40448 | Mindy      | Crissil    | Staff Scientist             |  94860 |      37270 |         1 |
|       56274 | Keriann    | Alloisi    | VP Marketing                | 110150 |      37270 |         1 |
|       63196 | Alaster    | Scutchin   | Assistant Professor         |  32179 |      37270 |         2 |
|       67009 | North      | de Clerc   | VP Product Management       | 114257 |      37270 |         2 |
|       67370 | Elladine   | Rising     | Social Worker               |  96767 |      37270 |         2 |
|       68249 | Nisse      | Voysey     | Financial Advisor           |  52832 |      37270 |         2 |
|       72540 | Guthrey    | Iacopetti  | Office Assistant I          | 117690 |      37270 |         3 |
|       72913 | Kass       | Hefferan   | Computer Systems Analyst IV |  96401 |      37270 |         3 |
|       75900 | Virge      | Goodrum    | Information Systems Manager |  54578 |      37270 |         3 |
|       76196 | Mirilla    | Janowski   | Cost Accountant             | 119241 |      37270 |         3 |
|       80529 | Lynde      | Aronson    | Junior Executive            |  77182 |      37270 |         4 |
|       80679 | Mildrid    | Sokale     | Geologist II                |  67987 |      37270 |         4 |
|       84791 | Hazel      | Tarbert    | General Manager             |  93760 |      37270 |         4 |
|       95213 | Cole       | Kesterton  | Pharmacist                  |  86119 |      37270 |         4 |
|       96513 | Theresa    | Binney     | Food Chemist                |  47354 |      37270 |         5 |
|       98374 | Estrellita | Daleman    | Staff Accountant IV         |  70187 |      37270 |         5 |
|      115357 | Ivy        | Fearey     | Structural Engineer         |  92710 |      37270 |         5 |
+-------------+------------+------------+-----------------------------+--------+------------+-----------+
*/

SELECT e.employee_id, e.first_name, e.last_name, m.first_name as manager_name
FROM employees e
JOIN employees m
ON e.reports_to = m.employee_id;

/*
+-------------+------------+-----------+--------------+
| employee_id | first_name | last_name | manager_name |
+-------------+------------+-----------+--------------+
|       33391 | D'arcy     | Nortunen  | Yovonnda     |
|       37851 | Sayer      | Matterson | Yovonnda     |
|       40448 | Mindy      | Crissil   | Yovonnda     |
|       56274 | Keriann    | Alloisi   | Yovonnda     |
|       63196 | Alaster    | Scutchin  | Yovonnda     |
|       67009 | North      | de Clerc  | Yovonnda     |
|       67370 | Elladine   | Rising    | Yovonnda     |
|       68249 | Nisse      | Voysey    | Yovonnda     |
|       72540 | Guthrey    | Iacopetti | Yovonnda     |
|       72913 | Kass       | Hefferan  | Yovonnda     |
|       75900 | Virge      | Goodrum   | Yovonnda     |
|       76196 | Mirilla    | Janowski  | Yovonnda     |
|       80529 | Lynde      | Aronson   | Yovonnda     |
|       80679 | Mildrid    | Sokale    | Yovonnda     |
|       84791 | Hazel      | Tarbert   | Yovonnda     |
|       95213 | Cole       | Kesterton | Yovonnda     |
|       96513 | Theresa    | Binney    | Yovonnda     |
|       98374 | Estrellita | Daleman   | Yovonnda     |
|      115357 | Ivy        | Fearey    | Yovonnda     |
+-------------+------------+-----------+--------------+
*/