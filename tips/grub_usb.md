```
# mkfs.ext3 -v -L "blah" /dev/<device>
# mount /dev/<device> /mnt
# cd /mnt
# grub-install  --no-floppy  --root-directory=. /dev/<device>
```
