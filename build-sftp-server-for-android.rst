How to build OpenSSH's sftp-server for Android
==============================================

Assuming you're using Debian (wheezy) GNU/Linux, install the following package:

  # apt-get install emdebian-archive-keyring

Then add this repository to `/etc/apt/sources.list.d/emdebian.sources.list`:

	# deb http://www.emdebian.org/debian squeeze main

Install the cross compiling tools for `arm`:

	# apt-get install g++-4.4-arm-linux-gnueabi
	# apt-get install xapt

And then needed libs for `OpenSSH` to build:

	# xapt -a armel -m zlib1g-dev
	# xapt -a armel -m libssl-dev

Fetch and uncompress `OpenSSH` (I used 6.2p2):

	$ wget -O- -q http://ftp2.fr.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-6.2p2.tar.gz|tar zxvf -

Apply the following (very dirty) patch:

::

	--- openssh-6.2p2/sftp-server-main.c	2009-02-21 22:47:02.000000000 +0100
	+++ openssh-6.2p2-android/sftp-server-main.c	2013-07-11 22:37:54.000000000 +0200
	@@ -40,12 +40,12 @@
	 
	 	/* Ensure that fds 0, 1 and 2 are open or directed to /dev/null */
	 	sanitise_stdfd();
	-
	+#if 0
	 	if ((user_pw = getpwuid(getuid())) == NULL) {
	 		fprintf(stderr, "No user found for uid %lu\n",
	 		    (u_long)getuid());
	 		return 1;
	 	}
	-
	+#endif
	 	return (sftp_server_main(argc, argv, user_pw));
	 }
	--- openssh-6.2p2/sftp-server.c	2013-01-09 05:58:22.000000000 +0100
	+++ openssh-6.2p2-android/sftp-server.c	2013-07-11 23:00:45.000000000 +0200
	@@ -1411,9 +1411,9 @@
	 
	 	__progname = ssh_get_progname(argv[0]);
	 	log_init(__progname, log_level, log_facility, log_stderr);
	-
	+#if 0
	 	pw = pwcopy(user_pw);
	-
	+#endif
	 	while (!skipargs && (ch = getopt(argc, argv, "d:f:l:u:cehR")) != -1) {
	 		switch (ch) {
	 		case 'R':
	@@ -1439,12 +1439,14 @@
	 			if (log_facility == SYSLOG_FACILITY_NOT_SET)
	 				error("Invalid log facility \"%s\"", optarg);
	 			break;
	+#if 0
	 		case 'd':
	 			cp = tilde_expand_filename(optarg, user_pw->pw_uid);
	 			homedir = percent_expand(cp, "d", user_pw->pw_dir,
	 			    "u", user_pw->pw_name, (char *)NULL);
	 			free(cp);
	 			break;
	+#endif
	 		case 'u':
	 			errno = 0;
	 			mask = strtol(optarg, &cp, 8);
	@@ -1471,10 +1473,10 @@
	 		*cp = '\0';
	 	} else
	 		client_addr = xstrdup("UNKNOWN");
	-
	+#if 0
	 	logit("session opened for local user %s from [%s]",
	 	    pw->pw_name, client_addr);
	-
	+#endif
	 	in = STDIN_FILENO;
	 	out = STDOUT_FILENO;

Fire up the `configure` script, note that we disable everything we can and ask
for a statically linked binary thanks to `--with-ldflags=-static`.

	./configure --host=arm-linux-gnueabi  --without-shadow --disable-largefile --disable-etc-default-login --disable-lastlog --disable-utmp --disable-utmpx --disable-wtmp --disable-wtmpx --disable-libutil --disable-pututline --disable-pututxline CC=/usr/bin/arm-linux-gnueabi-gcc --with-ldflags=-static

Build `sftp-server` the classic way:

	make sftp-server

And finally send it to your Android device via `adb`:

	adb push sftp-server /sdcard

The rest is up to you :)
