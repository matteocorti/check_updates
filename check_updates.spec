%define version 0.9.6
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
%__perl Makefile.PL  INSTALLSCRIPT=%{buildroot}%{_prefix} INSTALLSITEMAN1DIR=%{buildroot}/usr/share/man/man1
make

%install
make install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, 0644)
%doc AUTHORS Changes NEWS README INSTALL TODO COPYING VERSION
%attr(0755, root, root) %{_prefix}/%{name}
%attr(0755, root, root) /usr/share/man/man1/%{name}.1.gz

%changelog
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
