From [http://humdi.net/tips/index](http://humdi.net/tips/index)

### irssi

This short guide will tell you how to configure irssi so that it will keep showing ISO-8859-15 (or whatever you select) charset letters in terminal no matter what the other users on the channel are using. This way you won't need to worry anymore about UTF-8 junk messing with your terminal that uses ISO-8859-15 or the other way around. Here are the needed irssi commands:

```
/set termcharset ISO-8859-15
/set recodefallback ISO-8859-15
/set recodeoutdefaultcharset ISO-8859-15
/set recodetransliterate on
/set recodeautodetectutf8 on
/set recode on
/save
```

That should do it. There's no need to restart irssi assuming the terminal is really using the same charset as set in the term_charset variable. Further explanations about those commands can be obtained with

```
/help recode
```

### term

The purpose of this page is to describe how UTF-8 can be disable in Ubuntu / Debian console. At least Ubuntu releases starting from Dapper have UTF-8 enabled by default after a clean install has been done. Checking the current status is simple:

```
$ echo $LANG
en_US.UTF-8
```

If the result is anything else than en_US.UTF-8 then UTF-8 shouldn't be enabled and there's no point in reading the rest of this page unless generating locales is the point of interest.

Open `/etc/environment` as root (so that you can edit it) and it should by default look something like this:

```
PATH="/usr/sbin:/usr/bin:/sbin:/bin:/usr/bin/X11"
LANG="enUS.UTF-8"
LANGUAGE="en_FI:en"
```

The LANGUAGE setting depends of what you have selected during the beginning of the install process and usually doesn't nee to be changed. Remove UTF-8 from the LANG setting so that after editing that line will look like:

```
LANG="en_US"
```

Save the changes and close the file. Also check the content of `/etc/default/locale` if it exists and make the same change. At least in Gutsy it seems to override settings from the environment file. Next it's time to generate some new locales because en_US doesn't probably exist yet. Open `/var/lib/locales/supported.d/local` and if will look like:

```
en_US.UTF-8 UTF-8
```

and make it look like:

```
en_US ISO-8859-1
en_US.UTF-8 UTF-8
```

Also any other locale that needs to be generated should be added to that file. For example Finnish users might want to have fi_FI ISO-8859-1 in there too. Remeber to save the file after editing.

Now it's time to generate those new locales. As usual, run the following as root.

```
$ locale-gen Generating locales...
... Generation complete.
```

local-gen will list all locales included in /var/lib/locales/supported.d/local and generate those if necessary. Finally just log out and back in again. UTF-8 should now be disabled. That can be checked in the same way we started:

```
$ echo $LANG
en_US
```
