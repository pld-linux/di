Summary:	Disk Info
Summary(pl):	Disk Info
Name:		di
Version:	3.9
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.gentoo.com/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	59c840955175ffaf051417c5d0c702d3
URL:		http://www.gentoo.com/di/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
'di' is a disk information utility, displaying everything (and more)
that your 'df' command does. It features the ability to display your
disk usage in whatever format you desire/prefer/are used to.

It is designed to be portable across many platforms.

%description -l pl
'di' jest narzêdziem udostêpniaj±cym informacje o dyskach istniej±cych
w systemie. Podobnie jak 'df' lecz w bardziej przystêpnej formie.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
%{__make} RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README MANIFEST
%attr(755,root,root) %{_bindir}/di
%{_mandir}/man1/di.*
