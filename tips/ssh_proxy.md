```
host foo
UserKnownHostsFile /dev/null
StrictHostKeyChecking no
TCPKeepAlive yes
ServerAliveInterval 60
ProxyCommand ssh bar nc foo 22
```
