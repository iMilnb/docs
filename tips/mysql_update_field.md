```
mysql> update wp_options set option_value = 'http://foo.com/wordpress' where option_name = 'siteurl';
Query OK, 1 row affected (0.00 sec)
Rows matched: 1 Changed: 1 Warnings: 0
mysql> select * from wp_options where option_name = 'siteurl';
+-----------+---------+-------------+-------------------------------+----------+
| option_id | blog_id | option_name | option_value | autoload |
+-----------+---------+-------------+-------------------------------+----------+
| 1 | 0 | siteurl | http://foo.com/wordpress | yes |
+-----------+---------+-------------+-------------------------------+----------+
1 row in set (0.00 sec)
mysql>
```
