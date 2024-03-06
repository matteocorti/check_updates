
 &copy; Matteo Corti, ETH Zurich, 2007-2012

 &copy; Matteo Corti, 2007-2024

![](https://img.shields.io/github/v/release/matteocorti/check_updates)&nbsp;![](https://img.shields.io/github/downloads/matteocorti/check_updates/latest/total)&nbsp;![](https://img.shields.io/github/downloads/matteocorti/check_updates/total)&nbsp;![](https://img.shields.io/github/license/matteocorti/check_updates)&nbsp;![](https://img.shields.io/github/stars/matteocorti/check_updates)&nbsp;![](https://img.shields.io/github/forks/matteocorti/check_updates)


  see AUTHORS for the complete list of contributors

# check\_updates

check\_updates is a Nagios plugin to check if RedHat or Fedora system
is up-to-date

## Security

If at least a security update is available the plugin will return a critical status.
This can be overridden with the `--number-only` command line option

## DNF

DNF uses different caches per user. This has the consequence that DNF
and the plugin will potentially deliver different results for
different users.

## YUM security plugin

Use one of the following commands to install the YUM security plugin:

 - Fedora, Red Hat Enterprise Linux 6.x, CentOS 6.x, Scientific Linux 6.x systems:

```
yum install yum-plugin-security
```

 - Red Hat Enterprise Linux 5.x, CentOS 5.x and Scientific Linux 5.x systems:

```
yum install yum-security
```
