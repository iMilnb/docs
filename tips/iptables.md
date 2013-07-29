Authorize established connections

```
iptables -A INPUT -m state --state ESTABLISHED -j ACCEPT
```

Authorize specific port

```
iptables -A INPUT -p tcp -i eth0 --dport ssh -j ACCEPT
```
