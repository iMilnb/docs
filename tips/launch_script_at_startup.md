From [http://www.markomedia.com.au/osx/startup-script-for-apache-tomcat-on-snow-leopard-howto/](http://www.markomedia.com.au/osx/startup-script-for-apache-tomcat-on-snow-leopard-howto/)

1. Create your startup script:
```
sudo vim /usr/local/tomcat/bin/tomcat
#!/bin/sh # Tomcat Startup Script
CATALINA_HOME=/usr/local/tomcat; export CATALINA_HOME
JAVA_HOME=/Library/Java/Home; export JAVA_HOME
TOMCAT_OWNER=root; export TOMCAT_OWNER
 
start() {
	echo -n "Starting Tomcat: "
	su $TOMCAT_OWNER -c $CATALINA_HOME/bin/startup.sh
	sleep 2
}
 
stop() {
	echo -n "Stopping Tomcat: "
	su $TOMCAT_OWNER -c $CATALINA_HOME/bin/shutdown.sh
}
 
# See how we were called.
case "$1" in
	start)
	start
;;
	stop)
	stop
;;
	restart)
	stop
	start
;;
*)
 
echo $"Usage: tomcat {start|stop|restart}"
exit
esac
```

Set your TOMCAT_OWNER correctly.  You should run it as a valid system user.

2. Create a symbolic link in /usr/bin for easier access

```
sudo ln -s /usr/local/tomcat/bin/tomcat /usr/bin/tomcat
```

3. Create the startup daemon which will start Tomcat when the system boots up

```
sudo mkdir /Library/StartupItems/tomcat
sudo vim /Library/StartupItems/tomcat/tomcat
#!/bin/sh
. /etc/rc.common
 
# The start subroutine
StartService() {
# Insert your start command below.
tomcat start
}
 
# The stop subroutine
StopService() {
# Insert your stop command(s) below.
tomcat stop
}
 
# The restart subroutine
RestartService() {
# Insert your start command below.
tomcat restart
}
 
RunService "$1"
```

4. Create your startup parameters plist file

```
sudo vim /Library/StartupItems/tomcat/StartupParameters.plist
<?xml version="1.0" encoding="UTF-8"?> <!DOCTYPE plist SYSTEM "file://localhost/System/Library/DTDs/PropertyList.dtd">
<plist version="0.9">
	<dict>
		<key>Description</key>
		<string>Tomcat web server</string>
		<key>OrderPreference</key>
		<string>Late</string>
		<key>Provides</key>
		<array>
			<string>Local Web Services</string>
		</array>
		<key>Uses</key>
		<array>
			<string>SystemLog</string>
		</array>
	</dict>
</plist>
```
