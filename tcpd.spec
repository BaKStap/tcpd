Summary:	Another security wrapper for tcp daemons
Summary(pl):	Inny wrapper bezpiecze�stwa dla demon�w tcp
Name:		tcpd
Version:	980106
Release:	1
Copyright:	Distributable
Group:		Networking/Admin
Group(pl):	Sieciowe/Administracyjne
Vendor:		fujiwara@rcac.tdi.co.jp
Source0:	http://www.rcac.tdi.co.jp/fujiwara/%{name}-v6-0.0-%{version}.tar.gz
Patch0:		%{name}-linux.patch
URL:		http://www.rcac.tdi.co.jp/fujiwara/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	tcp_wrapper
Conflicts:	libwrap-static

%description
With this package you can monitor and filter incoming requests for the
SYSTAT, FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK, and other
network services. It is replacement for tcp_wrappers. It support both
- IPv4 and IPv6.

%description -l pl
Z tym pakietem mo�esz monitorowa� i filtrowa� nadchodz�ce pro�by do
SYSTAT, FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK, i innych
us�ug sieciowych. tcpd mo�e zast�pi� tcp_wrappers. tcpd wspiera
zar�wno IPv4 jak i IPv6.

%prep
%setup -q -n %{name}
%patch -p1

%build
OPT="$RPM_OPT_FLAGS" make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir} \
	$RPM_BUILD_ROOT{%{_libdir},%{_includedir},%{_sbindir}}

install libwrap.a $RPM_BUILD_ROOT%{_libdir}
install -s tcpd tcpd_check $RPM_BUILD_ROOT%{_sbindir}
install tcpd.h $RPM_BUILD_ROOT%{_includedir}
install hosts.access $RPM_BUILD_ROOT%{_sysconfdir}

gzip -9nf MEMO README.txt hosts.access

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/*
%attr(644,root,root) %config %verify(not md5 mtime size) %{_sysconfdir}/hosts.*
