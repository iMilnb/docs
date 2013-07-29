* Define your networks, along with your chosen names:

```
/network add -nick efnetnickname -user efnetusername -realname efnetrealname EFnet
/network add -nick freenodenickname -user freenodeusername -realname freenoderealname Freenode
```

* Add some servers to the networks and assign them to the networks:

```
/server add -network EFnet efnet.xs4all.nl /server add -network EFnet irc.dks.ca [...]

/server add -network Freenode asimov.freenode.net /server add -network Freenode lem.freenode.net [...]
```

* Save the settings:

```
/save
```

* Connect to the networks by just typing:

```
/connect EFnet /connect Freenode
```

irssi chooses one of the defined servers for each network and tries to connect. If a server fails, it tries the next one of those you defined.

If you need further help or want more options, have a look at these:

```
/help network /help server
```

Also, since you saved the settings, you can also take a look into the newly written irssi config file (`~/.irssi/config`).
