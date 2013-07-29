## DynDNS

* OpenBSD
* Standad BIND
* isc-dhcpd (ports)

```
# dnssec-keygen -a HMAC-MD5 -b 128 -n HOST DHCP
```

=> /var/named/etc/Kdhcp.+X+Y.private

*named.conf*

```
key "DHCP" {
    algorithm HMAC-MD5;
    secret "dakey";
};
// OU
include "/etc/rndc.key";
[...]
zone "home.imil.net" {
        type master;
        file "master/home.imil.net";
        allow-update {
                key "DHCP";
        };
};
```

*dhcpd.conf*

```
ddns-update-style interim;

authoritative;

key "DHCP" {
    algorithm HMAC-MD5;
    secret "dakey";
}
// OR
include "/etc/rndc.key";

zone home.imil.net {
        primary 127.0.0.1;
        key "DHCP";
}

zone 17.168.192.in-addr.arpa. {
        primary 127.0.0.1;
        key "DHCP";
}
```

Good doc: http://www.debian-administration.org/article/Configuring_Dynamic_DNS__DHCP_on_Debian_Stable
