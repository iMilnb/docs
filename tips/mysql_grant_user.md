```
$ mysql -u dbadmin -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 5340 to server version: 3.23.54

Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

mysql> CREATE DATABASE dbname;
Query OK, 1 row affected (0.00 sec)

mysql> GRANT ALL PRIVILEGES ON dbname.* TO "usertogrant"@"hote"
    -> IDENTIFIED BY "password";
Query OK, 0 rows affected (0.00 sec)
 
mysql> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.01 sec)
```
