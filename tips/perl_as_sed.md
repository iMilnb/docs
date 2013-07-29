From [http://oreilly.com/pub/h/73](http://oreilly.com/pub/h/73)

Print:

```
perl -pe 's/localhost/localhost $ENV{HOSTNAME}/' /etc/hosts
```

Replace without backup:

```
perl -pi -e 's/^(\s+)?(telnet|shell|login|exec)/# $2/' /etc/inetd.conf
```

Replace with backup:

```
perl -pi.orig -e 's/^(\s+)?(telnet|shell|login|exec)/# $2/' /etc/inetd.conf
```

Many replace with backup:

```
perl -pi.bak -e 's/bgcolor=#ffffff/bgcolor=#000000/i' *.html
```
