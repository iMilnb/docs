```
AuthUserFile /home/www/.htpasswd
AuthGroupFile /dev/null
AuthName "Access required" AuthType Basic

<Limit GET POST> Require valid-user </Limit>
```
