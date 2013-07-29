```
# tar zxvfp kern-GENERIC.tgz -C /
# shutdown -r now
```

If everything went well, you can proceed to upgrading the userland:

```
# for i in base comp games man misc modules tests text xbase xcomp xetc xfont xserver; do
tar zxvfp $i.tgz -C /
done
# mkdir /tmp/tmproot
# tar zxvfp etc.tgz -C /tmp/tmproot
# postinstall -s /tmp/tmproot check
# (.. run the command postinstall gave you ..)
# etcupdate -s /tmp/tmproot
# shutdown -r now
```
