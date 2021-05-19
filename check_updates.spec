%define version          1.8.1
%define release          0
%define sourcename       check_updates
%define packagename      nagios-plugins-check-updates
%define nagiospluginsdir %{_libdir}/nagios/plugins

# No binaries in this package
%define debug_package    %{nil}

Summary:       A Nagios plugin to check if RedHat or Fedora system is up-to-date
Name:          %{packagename}
Version:       %{version}
Obsoletes:     check_updates
Release:       %{release}%{?dist}
License:       GPLv3+
Packager:      Matteo Corti <matteo@corti.li>
Group:         Applications/System
BuildRoot:     %{_tmppath}/%{packagename}-%{version}-%{release}-root-%(%{__id_u} -n)
URL:           https://github.com/matteocorti/check_updates
Source:        https://github.com/matteocorti/%{sourcename}/releases/download/v%{version}/%{sourcename}-%{version}.tar.gz

# Fedora build requirement (not needed for EPEL{4,5})
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
BuildRequires: perl(Readonly)

Requires:      nagios-plugins
# Yum security plugin RPM:
#    Fedora             : yum-plugin-security (virtual provides yum-security)
#    Red Hat Enterprise : yum-security
# Requires:  yum-security

%description
A Nagios plugin to check if RedHat or Fedora system is up-to-date

%prep
%setup -q -n %{sourcename}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor \
    INSTALLSCRIPT=%{nagiospluginsdir} \
    INSTALLVENDORSCRIPT=%{nagiospluginsdir}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name "*.pod" -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*

%check
make test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS Changes NEWS README.md COPYING COPYRIGHT
%{nagiospluginsdir}/%{sourcename}
%{_mandir}/man1/%{sourcename}.1*

%changelog
* Wed May   19 2021  <matteo@corti.li> - 1.8.1-0
- Updated to 1.8.1

* Thu Apr   15 2021  <matteo@corti.li> - 1.8.0-0
- Updated to 1.8.0

* Thu Jan   21 2021  <matteo@corti.li> - 1.7.13-0
- Updated to 1.7.13

* Fri Jun   19 2020  <matteo@corti.li> - 1.7.12-0
- Updated to 1.7.12

* Fri Jun   5 2020  <matteo@corti.li> - 1.7.11-0
- Updated to 1.7.11

* Thu Mar 12 2020  <matteo@corti.li> - 1.7.10-0
- Updated to 1.7.10

* Wed Feb 26 2020  <matteo@corti.li> - 1.7.9-0
- Updated to 1.7.9
w
* Sat Dec 28 2019  <matteo@corti.li> - 1.7.8-0
- Updated to 1.7.8

* Wed Dec 11 2019  <matteo@corti.li> - 1.7.7-0
- Updated to 1.7.7

* Tue Oct 29 2019  <matteo@corti.li> - 1.7.6-0
- Updated to 1.7.6

* Mon Aug  5 2019  <matteo@corti.li> - 1.7.4-0
- Updated to 1.7.4

* Thu Jun 13 2019  <matteo@corti.li> - 1.7.3-0
- Updated to 1.7.3

* Tue May  7 2019  <matteo@corti.li> - 1.7.2-0
- Updated to 1.7.2

* Mon Feb 11 2019  <matteo@corti.li> - 1.7.1-0
- Updated to 1.7.1

* Wed Dec 19 2018  <matteo@corti.li> - 1.7.0-0
- Updated to 1.7.0

* Fri Nov 30 2018  <matteo@corti.li> - 1.6.25-0
- Updated to 1.6.25

* Tue Nov 27 2018  <matteo@corti.li> - 1.6.24-0
- Updated to 1.6.24

* Tue Jun 19 2018  <matteo@corti.li> - 1.6.23-0
- Updated to 1.6.23

* Wed Jun 13 2018  <matteo@corti.li> - 1.6.22-0
- Updated to 1.6.22

* Tue May 22 2018  <matteo@corti.li> - 1.6.21-0
- Updated to 1.6.21

* Tue Jul 18 2017  <matteo@corti.li> - 1.6.20-0
- Updated to 1.6.20

* Tue Jan  3 2017  <matteo@corti.li> - 1.6.19-0
- Updated to 1.6.19

* Mon May 30 2016  <matteo@corti.li> - 1.6.18-0
- Updated to 1.6.18

* Thu May 26 2016  <matteo@corti.li> - 1.6.17-0
- Updated to 1.6.17

* Mon Apr 18 2016  <matteo@corti.li> - 1.6.16-0
- Updated to 1.6.16

* Wed Jan 20 2016  <matteo@corti.li> - 1.6.15-0
- Updated to 1.6.15

* Thu Jan 14 2016  <matteo@corti.li> - 1.6.14-0
- Updated to 1.6.14

* Tue Jan 12 2016  <matteo@corti.li> - 1.6.13-0
- Updated to 1.6.13

* Fri Aug 28 2015  <matteo@corti.li> - 1.6.12-0
- Updated to 1.6.12

* Thu Aug 27 2015 Matteo Corti <matteo@corti.li> - 1.6.11-0
- Updated to 1.6.11

* Thu Aug 27 2015 Matteo Corti <matteo.corti@id.ethz.ch> - 1.6.10-0
- Updated to 1.6.10

* Sun Dec 28 2014 Matteo Corti <matteo@corti.li> - 1.6.9-0
- Updated to 1.6.9

* Sun Sep 21 2014 Matteo Corti <matteo@corti.li> - 1.6.8-0
- Updated to 1.6.8

* Fri May 23 2014 Matteo Corti <matteo.corti@id.ethz.ch> - 1.6.7-0
- Updated to 1.6.7

* Thu Oct 10 2013 Matteo Corti <matteo.corti@id.ethz.ch> - 1.6.6-0
- Updated to 1.6.6 (openvz kernel support)

* Mon Jul 15 2013 Matteo Corti <matteo.corti@id.ethz.ch> - 1.6.5-0
- Updated to 1.6.5 (disabled ePN)

* Tue Jun 18 2013 Matteo Corti <matteo.corti@id.ethz.ch> - 1.6.4-0
- Updated to 1.6.4 (handle wide Yum output)

* Sat May 11 2013 Matteo Corti <matteo.corti@id.ethz.ch> - 1.6.3-0
- Updated to 1.6.3 (no security perf data if Yum security plugin is not installed)

* Fri Mar 29 2013 Matteo Corti <matteo.corti@id.ethz.ch> - 1.6.2-0
- Updated to 1.6.2 (Yum arguments patch)

* Mon Sep  3 2012 Matteo Corti <matteo.corti@id.ethz.ch> - 1.6.1-0
- Updated to 1.6.1 (PUIAS Linux)

* Sun Apr 15 2012 Matteo Corti <matteo.corti@id.ethz.ch> - 1.6.0-0
- Updated to 1.6.0 (--security-only option)

* Sun Dec  4 2011 Matteo Corti <matteo.corti@id.ethz.ch> - 1.5.2-0
- Updated to 1.5.2 (bug fix release)

* Sat Dec  3 2011 Matteo Corti <matteo.corti@id.ethz.ch> - 1.5.1-0
- Support for Amazon Linux

* Mon Oct  3 2011 Matteo Corti <matteo.corti@id.ethz.ch> - 1.5.0-0
- Updated to 1.5.0 (fixed a bug which caused -w and -c to be ignored)

* Fri Sep 23 2011 Matteo Corti <matteo.corti@id.ethz.ch> - 1.4.15-0
- Updated to 1.4.15 (which now uses /etc/redhat-release instead of /etc/issue)

* Wed May 25 2011 Matteo Corti <matteo.corti@id.ethz.ch> - 1.4.14-0
- Fixed a runtime check on correct command execution

* Tue May 24 2011 Matteo Corti <matteo.corti@id.ethz.ch> - 1.4.13-0
- fixed the unit tests on RH systems (old Test::Simple version)
- added the unit tests to the build process

* Tue May 24 2011 Matteo Corti <matteo.corti@id.ethz.ch> - 1.4.12-0
- fixed the detection of RH 6 and Scientific Linux Systems

* Thu Nov 18 2010 Matteo Corti <matteo.corti@id.ethz.ch> - 1.4.11-0
- fixed the processing of Xen kernels

* Mon Nov 15 2010 Matteo Corti <matteo.corti@id.ethz.ch> - 1.4.10-0
- License fix and new package name

* Mon Nov  1 2010 Matteo Corti <matteo.corti@id.ethz.ch> - 1.4.9-0
- removed the dependency on version.pm

* Sun Oct 31 2010 Matteo Corti <matteo.corti@id.ethz.ch> - 1.4.8-0
- updated to 1.4.8 (fixed the license declaration)

* Tue Feb 16 2010 Matteo Corti <matteo.corti@id.ethz.ch> - 1.4.7-0
- updated to 1.4.7 (bug fix: wrong update count if yum check-updates gets wrapped)

* Thu Dec 10 2009 Matteo Corti <matteo.corti@id.ethz.ch> - 1.4.6-0
- updated to 1.4.6 (man page installed in 1, installation and packaging fixes)

* Tue Dec  8 2009 Matteo Corti <matteo.corti@id.ethz.ch> - 1.4.5-0
- updated to 1.4.5 (fixed OK status message on up2date based systems)

* Mon Dec  7 2009 Matteo Corti <matteo.corti@id.ethz.ch> - 1.4.4-0
- updated to 1.4.4 (SMP version cleanup bug)

* Mon Dec  7 2009 Matteo Corti <matteo.corti@id.ethz.ch> - 1.4.3-0
- updated to 1.4.3 (PAE version cleanup bug)

* Mon Dec  7 2009 Matteo Corti <matteo.corti@id.ethz.ch> - 1.4.2-0
- updated to 1.4.2 (patches from J. Oliveira)

* Sun Dec  6 2009 Matteo Corti <matteo.corti@id.ethz.ch> - 1.4.1-0
- updated to 1.4.1 (minor fixes)

* Fri Dec  4 2009 Matteo Corti <matteo.corti@id.ethz.ch> - 1.4.0-0
- updated 1.4.0 (checks for security updates if yum-plugin-security is available )

* Wed Nov 11 2009 Matteo Corti <matteo.corti@id.ethz.ch> - 1.3.4-0
- Updated to 1.3.4

* Sun Sep 20 2009 Matteo Corti <matteo.corti@id.ethz.ch> - 1.3.3-0
- Updated to 1.3.3

* Wed Jul 22 2009 Matteo Corti <matteo.corti@id.ethz.ch> - 1.3.2-0
- fixed a bug which gave wrong results on systems with a non-English localizations

* Mon Jun 15 2009 Matteo Corti <matteo.corti@id.ethz.ch> - 1.3.1-0
- support for PAE kernels

* Wed May 20 2009 Matteo Corti <matteo.corti@id.ethz.ch> - 1.3.0-2
- RPM is now relocatable

* Tue May 19 2009 Matteo Corti <matteo.corti@id.ethz.ch> - 1.3.0-1
- --critical and --working working again + support for extended info

* Tue Apr  7 2009 Matteo Corti <matteo.corti@id.ethz.ch> - 1.2.3-0
- RH5 support

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

* Thu May  8 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 1.0.0-0
- correct kernel version comparisons

* Mon Mar 17 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.13-0
- bug fix for up2date kernel on CentOS

* Fri Mar  7 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.12-0
- fixed a bug in the reboot notification

* Tue Feb 26 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.11-0
- fixed a bug in the package count

* Thu Feb 21 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.10-0
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
