Build and run dropbear with sftp support for Android
====================================================

So now that there's no clean way of mounting your new Jelly Bean Android device as a mass-storage device, you're trying to find a simple way of sharing files from/to your Android device. The [SSHFS][1] filesystem is a convenient way of accessing a `SSH` filesystem, but obviously it has some pre-requisites on the target device:

* An `SSH` server
* `sftp-server` support

There are some `SSH` servers available on the Android market, or better said "SSH server GUIs". They are all based on `dropbear` 0.52, which is pretty old, and  they actually provide binaries which we really can't say where and how they were built. Also, none of those provide an out-of-the-box working `sftp-server`, which is mandatory to use [SSHFS][1].

This document aims at explaining how to build your own `dropbear` and `sftp-servers` binaries, and how to use them.

![SSH access to a SG4](https://raw.github.com/iMilnb/docs/master/images/dropsftp.png)

Cross-compiling pre-requisites
------------------------------

* Assuming you're using Debian (wheezy) GNU/Linux, install the following package

```
# apt-get install emdebian-archive-keyring
```

* Then add this repository to `/etc/apt/sources.list.d/emdebian.sources.list`

```
# deb http://www.emdebian.org/debian squeeze main
```

* Install the cross compiling tools for `arm`

```
# apt-get install g++-4.4-arm-linux-gnueabi
# apt-get install xapt
```

* And then needed libs for `OpenSSH` to build `sftp-server`

```
# xapt -a armel -m zlib1g-dev
# xapt -a armel -m libssl-dev
```

Build dropbear
--------------

* Fetch and uncompress [dropbear][2]

```
$ wget -O- -q https://matt.ucc.asn.au/dropbear/dropbear-2013.58.tar.bz2|tar jxvf -
```

* Apply the following [dropbear patch][3] (based on dropbear/Android patch by Jakob Blomer)

```
$ cd dropbear-2013.58
$ patch < dropbear-2013-58-android.patch
```

* Fire up the `configure` script with the following options

```
	$ ./configure --host=arm-linux-gnueabi --disable-zlib --disable-largefile --disable-loginfunc --disable-shadow --disable-utmp --disable-utmpx --disable-wtmp --disable-wtmpx --disable-pututline --disable-pututxline --disable-lastlog --disable-syslog CC=/usr/bin/arm-linux-gnueabi-gcc
```

* Tune up the `options.h` file according to your needs or [fetch mine][4]

* Build dropbear with those variables set

```
$ STATIC=1 MULTI=1 CC=arm-linux-gnueabi-gcc SCPPROGRESS=0 PROGRAMS="dropbear dropbearkey scp dbclient" make strip
```

* Push the `dropbearmulti` binary to a writable directory of your `android` device

```
$ adb push dropbearmulti /sdcard/tmp
```

Build sftp-server
-----------------

* Fetch and uncompress `OpenSSH` (2013/07 latest version is 6.2p2)

```
$ wget -O- -q http://ftp2.fr.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-6.2p2.tar.gz|tar zxvf -
```

* Apply the following [(very dirty) patch][5]

```
$ cd openssh-6.2p2
$ patch < sftp-server-android.patch
```

* Fire up the `configure` script, note that we disable everything we can and ask for a statically linked binary thanks to `--with-ldflags=-static`.

```
$ ./configure --host=arm-linux-gnueabi  --without-shadow --disable-largefile --disable-etc-default-login --disable-lastlog --disable-utmp --disable-utmpx --disable-wtmp --disable-wtmpx --disable-libutil --disable-pututline --disable-pututxline CC=/usr/bin/arm-linux-gnueabi-gcc --with-ldflags=-static
```

* Build `sftp-server` the classic way:

```
$ make sftp-server
```

And finally send it to your Android device via `adb`:

```
$ adb push sftp-server /sdcard/tmp
```

Prepare your device for dropbear
--------------------------------

* Create needed directories

```
$ adb shell
$ su
# mkdir -p /data/dropbear/{bin,etc,var}
# cd /data/dropbear
```

* Copy previously pushed binaries to `dropbear`'s `bin` directory

```
# cp /sdcard/tmp/{dropbearmulti,sftp-server} bin/
```

* `dropbearmulti` is a multi-call binary, it is required to create the actual programs symlinks

```
# cd bin
# ln -s dropbearmulti dropbear
# ln -s dropbearmulti dropbearkey
# ln -s dropbearmulti dbclient
# ln -s dropbearmulti scp
```

* Create needed private and public keys for this device

```
# bin/dropbearkey -t rsa -f etc/dropbear_rsa_host_key
# bin/dropbearkey -t dss -f etc/dropbear_dss_host_key
# bin/dropbearkey -t rsa -f etc/id_rsa
# bin/dropbearkey -f etc/id_rsa -y > etc/id_rsa.pub
```

* Populate the `authorized_keys` file

```
# cat > etc/authorized_keys
<paste here the authorized id_{rsa,dsa}.pub keys>
^D
```

* Try `dropbear` by launching it as a foreground process

```
# bin/dropbear -A -N shell -U 1000 -G 1000 -R etc/authorized_keys -F
```

* In order to be able to use `scp`, it must be seen on `$PATH`

```
# mount -o remount,rw /system
# ln -s /data/dropbear/bin/dropbearmulti /system/xbin/scp
# mount -o remount,ro /system
```

Run `dropbear` as a daemon
--------------------------

* Once everything works as expected, simply start `dropbear` without the `-F` flag and with full path to `authorized_keys`

```
# bin/dropbear -A -N shell -U 1000 -G 1000 -R /data/dropbear/etc/authorized_keys
```

* From now on, you will be able to access your device through `SSH`, but also through `SFTP`, thus making is "mountable" using [SSHFS][1].

Useful URLs
-----------

* http://wiki.debian.org/EmdebianToolchain
* http://wiki.cyanogenmod.org/w/Doc:_dropbear
* http://blog.mwmdev.com/tutorials/249/
* https://matt.ucc.asn.au/dropbear/
* https://github.com/rngadam/XinCheJian-GGHC/wiki/Installing-and-using-ssh-server-on-android
* https://code.google.com/p/droidsshd/wiki/BuildingDropbear
* http://adrianpopagh.blogspot.fr/2013/01/android-adding-scpsftp-support-to.html
* http://www.brandonhutchinson.com/Installing_OpenSSH.html
* https://code.google.com/p/droidsshd/issues/detail?id=1

[1]: http://fuse.sourceforge.net/sshfs.html
[2]: https://matt.ucc.asn.au/dropbear/
[3]: patches/dropbear-2013-58-android.patch
[4]: patches/options.h
[5]: patches/openssh-6.2p2-android.patch
