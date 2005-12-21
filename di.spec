Summary:	Disk Info - disk information utility
Summary(pl):	Disk Info - informacje o dyskach 
Name:		di
Version:	4.4
Release:	1
License:	custom (see LICENSE* files)
Group:		Applications/System
Source0:	http://www.gentoo.com/di/%{name}-%{version}.tar.gz
# Source0-md5:	222a367414030666690e833fc2668be4
URL:		http://www.gentoo.com/di/
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
'di' is a disk information utility, displaying everything (and more)
that your 'df' command does. It features the ability to display your
disk usage in whatever format you desire/prefer/are used to.

It is designed to be portable across many platforms.

%description -l pl
'di' jest narzêdziem udostêpniaj±cym informacje o dyskach istniej±cych
w systemie - podobnie jak 'df', lecz w bardziej przystêpnej formie. Ma
mo¿liwo¶æ wy¶wietlania wykorzystania dysku w dowolnie wybranym
formacie.

Jest zaprojektowane w sposób przeno¶ny na wiele platform.

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
