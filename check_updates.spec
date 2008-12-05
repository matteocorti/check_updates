%define version 1.2.2
%define release 0
%define name    check_updates
%define _prefix /usr/lib/nagios/plugins/contrib

Summary:   A Nagios plugin to check if RedHat or Fedora system is up-to-date
Name:      %{name}
Version:   %{version}
Release:   %{release}
License:   GPL
Packager:  Matteo Corti <matteo.corti@id.ethz.ch>
Group:     Applications/System
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Source:    http://www.id.ethz.ch/people/allid_list/corti/%{name}-%{version}.tar.gz
BuildArch: noarch

Requires: perl

%description
A Nagios plugin to check if RedHat or Fedora system is up-to-date

%prep
%setup -q

%build
%__perl Makefile.PL  INSTALLSCRIPT=%{buildroot}%{_prefix} INSTALLSITEMAN3DIR=%{buildroot}/usr/share/man/man3 INSTALLSITESCRIPT=%{buildroot}%{_prefix}
make

%install
make install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, 0644)
%doc AUTHORS Changes NEWS README INSTALL TODO COPYING VERSION
%attr(0755, root, root) %{_prefix}/%{name}
%attr(0755, root, root) /usr/share/man/man3/%{name}.3pm.gz

%changelog
* Fri Dec  5 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 1.2.2-0
- bug fixes

* Fri Dec  5 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 1.2.0-0
- update to 1.2.0 (timeout and no dep on RPM2)

* Fri Nov 14 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 1.1.2-0
- fixed a bug with up2date and excluded packages

* Wed Aug  6 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 1.1.1-0
- fixed a problem with RPM version numbers

* Tue Jun  3 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 1.0.2-0
- separated POD because of ePN issues

* Thu May 15 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 1.0.1-0
- removing the trailing arch from uname

* Thu May  8 2008 root <matteo.corti@id.ethz.ch> - 1.0.0-0
- correct kernel version comparisons

* Mon Mar 17 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.13-0
- bug fix for up2date kernel on CentOS

* Fri Mar  7 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.12-0
- fixed a bug in the reboot notification

* Tue Feb 26 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.11-0
- fixed a bug in the package count

* Thu Feb 21 2008 root <matteo.corti@id.ethz.ch> - 0.9.10-0
- fixed kernel check on RH

* Thu Feb 21 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.9-0
- checks if the running kernel is the latest installed

* Tue Jan 22 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.8-0
- Considers CentOS

* Thu Dec 13 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.7-0
- performance data

* Thu Nov 29 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.6-0
- corrected the plugin name

* Thu Nov 29 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.5-0
- checks for root

* Thu Nov 29 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.4-0
- removed sudo

* Thu Nov 29 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.3-0
- New version: up2date requires sudo

* Thu Nov 29 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.2-0
- Initial test package

* Thu Nov 29 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.1-0
- Initial test package
