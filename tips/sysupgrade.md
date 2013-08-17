## Safely upgrade a NetBSD system with sysupgrade

I don't rely on [sysupgrade](http://blog.netbsd.org/tnf/entry/introducing_sysbuild_and_sysupgrade) to upgrade the kernel, mainly because you may end up with incompatibles userland / kernel at some point. This is why I won't recommend the `auto` keyword. Instead, I first upgrade the kernel, which is backward compatible, then use *sysupgrade(8)* to update the userland.
Also, in most cases, as I build my own *NetBSD* kernels in order to enable IPsec and some additional features, there's no real need for *sysupgrade(8)* in that area.
For most people, the following procedure will do:

### Upgrade the kernel

```
$ ftp ftp://ftp.fr.netbsd.org/pub/NetBSD/NetBSD-6.1/amd64/binary/kernel/netbsd-GENERIC.gz
# cp /netbsd /onetbsd
# cp netbsd-GENERIC.gz /netbsd
```

### Reboot with the new kernel

```
# shutdown -r now
```

`uname -r` should show the new kernel version.

### Fetch the release sets

```
# sysupgrade fetch ftp://ftp.fr.NetBSD.org/pub/NetBSD/NetBSD-6.1/$(uname -m)
```

### Install the new sets

```
# sysupgrade sets
```

### Post-install

```
# sysupgrade postinstall
```

### Update /etc

```
# sysupgrade etcupdate
```

### Cleanup downloaded archives

```
# sysupgrade clean
```

## Reboot in order to re-run updated `/etc/rc.d` scripts

```
# shutdown -r now
```

## Profit!
