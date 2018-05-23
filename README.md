
 (c) Matteo Corti, ETH Zurich, 2007-2012

 (c) Matteo Corti, 2007-2018

  see AUTHORS for the complete list of contributors

# check_updates

check_updates is a Nagios plugin to check if RedHat or Fedora system
is up-to-date

The plugin uses either YUM, DNF or up2date depending on the operating
system.

## up2date

since up2date -l to list the outdated packages can only be run be run
by root the plugin must be executed as root. Please configure sudo as
follows:

```
nagios ALL= NOPASSWD: /usr/sbin/up2date -l
```

and execute the plugin with sudo

```
sudo $INSTALLATION_PATH/check_updates
```

## DNF

DNF uses different caches per user. This has the consequence that DNF
and the plugin will potentially deliver different results for
different users.

## Yum security plugin

Use one of the following commands to install the yum security plugin:

 - Fedora, Red Hat Enterprise Linux 6.x, CentOS 6.x, Scientific Linux 6.x systems:

```
yum install yum-plugin-security
```

 - Red Hat Enterprise Linux 5.x, CentOS 5.x and Scientific Linux 5.x systems:

```
yum install yum-security
```