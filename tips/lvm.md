```
pvcreate /dev/sda1 /dev/sdb1
vgcreate foo /dev/sda1 /dev/sdb1
vgrename foo bar
lvcreate -L10G -n mylv bar
lvremove /dev/bar/mylv

```
