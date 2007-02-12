Summary:	Disk Info - disk information utility
Summary(pl.UTF-8):   Disk Info - informacje o dyskach
Name:		di
Version:	4.9
Release:	1
License:	custom (see LICENSE* files)
Group:		Applications/System
Source0:	http://www.gentoo.com/di/%{name}-%{version}.tar.gz
# Source0-md5:	d71682678fc950b64f9ffff8a7587505
URL:		http://www.gentoo.com/di/
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
'di' is a disk information utility, displaying everything (and more)
that your 'df' command does. It features the ability to display your
disk usage in whatever format you desire/prefer/are used to.

It is designed to be portable across many platforms.

%description -l pl.UTF-8
'di' jest narzędziem udostępniającym informacje o dyskach istniejących
w systemie - podobnie jak 'df', lecz w bardziej przystępnej formie. Ma
możliwość wyświetlania wykorzystania dysku w dowolnie wybranym
formacie.

Jest zaprojektowane w sposób przenośny na wiele platform.

%prep
%setup -q

%build
%{__make} \
	prefix=%{_prefix} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{de_DE,de}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README MANIFEST LICENSE*
%attr(755,root,root) %{_bindir}/di
%attr(755,root,root) %{_bindir}/mi
%{_mandir}/man1/di.*
