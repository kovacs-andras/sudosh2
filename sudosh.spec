#	$Id: sudosh.spec,v 1.2 2010/07/09 20:05:53 squash Exp $
#
%define origname sudosh2
%define name sudosh2
%define version 1.0.7
%define release 3.el7

Name: %{name}
Version: %{version}
Release: %{release}
Summary: Logged root shell that can be used for auditing

Group: System/SDL-custom
License: OSL
URL: https://github.com/kovacs-andras/sudosh2/
Source: https://github.com/kovacs-andras/sudosh2/archive/%{version}-%{release}.zip

Packager: Andras Kovacs <andras0602@hotmail.com>
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: x86_64
Requires: sudo
Provides: %{origname} = %{version}-%{release}, %{name} = %{version}-%{release}

%description
sudosh2 is the default login shell for AD-based users.
See more here:
https://go.sap.corp/sudosh2
https://go.sap.corp/sudosh2-troubleshoot

%prep
%setup -q -n %{origname}-%{version}

%{__cat} <<EOF >sudosh.conf.tmp
# Sudosh Configuration File
logdir                  = /var/log/sudosh
default shell           = /bin/bash
delimiter               = -
syslog.priority         = LOG_INFO
syslog.facility         = LOG_LOCAL2
clearenvironment        = yes

# Allow Sudosh to execute -c arguements?  If so, what?
-c arg allow = scp
-c arg allow = sftp
-c arg allow = /usr/libexec/openssh/sftp-server
-c arg allow = rsync
-c arg allow = screen
-c arg allow = tmux
EOF

%build
%configure \
	--program-prefix="%{?_program_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
mkdir -p %{buildroot}/var/log/sudosh
install -m 0744 sudosh.conf.tmp %{buildroot}/etc/sudosh.conf

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man1/sudosh.1*
%doc %{_mandir}/man5/sudosh.conf*
%doc %{_mandir}/man8/sudosh-replay.8*
%{_bindir}/sudosh
%{_bindir}/sudosh-replay
%config(noreplace) %{_sysconfdir}/sudosh.conf
%dir %attr(0733 root root) /var/log/sudosh

%changelog
* Thu Jan 28 2021 Andras Kovacs <andras0602@hotmail.com> - 1.0.7-3
- Update for version 1.0.7
- Custom HXM sudosh.conf
- Description with URLs
* Tue Jul 16 2019 - 1.0.7
- Fixed ompilation errors for newer gcc
- Version bumped to 1.0.7
* Wed Apr 29 2015 - 1.0.6
- Version bumped to 1.0.6
* Fri Jul 09 2010 John Barton <jbarton@technicalworks.net> - 1.0.4-1
- Update for version 1.0.4

