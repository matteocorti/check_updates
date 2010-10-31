################################################################################
# File version information:
# $Id$
# $Revision$
# $HeadURL$
# $Date$
################################################################################

%define version 1.4.7
%define release 0
%define name    check_updates
%define nagiospluginsdir %{_libdir}/nagios/plugins

# No binaries in this package
%define debug_package %{nil}

Summary:   A Nagios plugin to check if RedHat or Fedora system is up-to-date
Name:      %{name}
Version:   %{version}
Release:   %{release}%{?dist}
License:   GPLv3+
Packager:  Matteo Corti <matteo.corti@id.ethz.ch>
Group:     Applications/System
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
URL:       https://trac.id.ethz.ch/projects/nagios_plugins/wiki/check_updates
Source:    https://trac.id.ethz.ch/projects/nagios_plugins/downloads/%{name}-%{version}.tar.gz

# Fedora build requirement (not needed for EPEL{4,5})
BuildRequires: perl(ExtUtils::MakeMaker)

Requires:  nagios-plugins
# Yum security plugin RPM:
#    Fedora             : yum-plugin-security (virtual provides yum-security)
#    Red Hat Enterprise : yum-security
# Requires:  yum-security

%description
A Nagios plugin to check if RedHat or Fedora system is up-to-date

%prep
%setup -q

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

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS Changes NEWS README TODO COPYING COPYRIGHT
%{nagiospluginsdir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Sun Oct 31 2010 Matteo Corti <matteo.corti@id.ethz.ch> - 1.4.7-0
- updated to 1.4.8 (fixed the license declaration)

* Tue Feb 16 2010 root <matteo.corti@id.ethz.ch> - 1.4.7-0
- updated to 1.4.7 (bug fix: wrong update count if yum check-updates gets wrapped)

* Thu Dec 10 2009 Matteo Corti <matteo.corti@id.ethz.ch> - 1.4.6-0
- updated to 1.4.6 (man page installed in 1, installation and packaging fixes)

* Tue Dec  8 2009 Matteo Corti <matteo.corti@id.ethz.ch> - 1.4.5-0
- updated to 1.4.5 (fixed OK status message on up2date based systems)

* Mon Dec  7 2009 Matteo Corti <matteo.corti@id.ethz.ch> - 1.4.4-0
- updated to 1.4.4 (SMP version cleanup bug)

* Mon Dec  7 2009 root <matteo.corti@id.ethz.ch> - 1.4.3-0
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
