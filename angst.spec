Summary:	Active sniffer
Summary(pl):	Aktywny sniffer
Name:		angst
Version:	0.4b
Release:	1
License:	BSD
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/angst/%{name}-%{version}.tar.gz
# Source0-md5:	21643cd776bf478c6fbe4ddabb826be8
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-libnet.patch
URL:		http://angst.sourceforge.net/
BuildRequires:	libnet1-devel
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Angst is an active sniffer, based on libpcap and libnet. Angst
provides methods for aggressive sniffing on switched local area
network environments. It dumps the payload of all the TCP packets
received on the specified ports. Moreover, it implements methods for
active sniffing. Angst currently provides two active sniffing methods.
The first monitors ARP requests, and after enabling IP forwarding on
the local host, sends ARP replies mapping all IPs to the local MAC
address. The second method floods the local network with random MAC
addresses (like macof v1.1 by Ian Vitek), causing switches to send
packets to all ports.

%description -l pl
Angst to aktywny sniffer, oparty na libpcap i libnet. Angst dostarcza
metody do agresywnego sniffowania w �rodowiskach lokalnych
switchowanych sieci. Zrzuca payload wszystkich pakiet�w TCP odebranych
na podanych portach. Co wi�cej, ma zaimplementowane (aktualnie dwie)
metody aktywnego sniffowania. Pierwsza to monitorowanie ��da� ARP i po
w��czeniu przekazywania IP na lokalnej maszynie wysy�anie odpowiedzi
ARP przekierowuj�cych ca�e IP na lokalny adres MAC. Druga to
floodowanie sieci lokalnej losowymi adresami MAC (podobnie do macof
v1.1 Iana Vitka), co powoduje, �e switche wysy�aj� pakiety na
wszystkie porty.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

mv -f Makefile.linux Makefile

%build
%{__make} \
	CC="%{__cc}"
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/%{name}.8*
