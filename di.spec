Summary:	Disk Info 
Summary(pl):	Disk Info
Name:		di
Version:	2.3
Release:	1
Copyright:	GPL
Group:		System Tools
Group(pl):	Na¿êdzia systemowe
Source0:	%name-distr.001
Source1:	%name-distr.002
Source2:	%name-distr.003
#BuildRequires:	
#Requires:	
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr

%description
'di' is a disk information utility, displaying everything (and more) that 
your 'df' command does. It features the ability to display your disk usage 
in whatever format you desire/prefer/are used to. 

It is designed to be portable across many platforms.

%description -l pl
'di' jest narzêdziem udostêpniaj±cym informacje o dyskach istniej±cych 
w systemie. Podobnie jak 'df' lecz w bardziej przystêpnej formie.

%prep
rm -fr $RPM_BUILD_DIR/%name-%version 
install -d $RPM_BUILD_DIR/%name-%version
STATUS=$?
if [ $STATUS -ne 0 ]; then
    exit STATUS
fi    
cd $RPM_BUILD_DIR/%name-%version
STATUS=$?
if [ $STATUS -ne 0 ]; then
    exit STATUS
fi    
sh %{SOURCE0}
sh %{SOURCE1}
sh %{SOURCE2}
STATUS=$?
if [ $STATUS -ne 0 ]; then
    exit STATUS
fi    

%build
cd $RPM_BUILD_DIR/%name-%version
./configure --prefix=%{_prefix}
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
cd $RPM_BUILD_DIR/%name-%version
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
make PREFIX=$RPM_BUILD_ROOT%{_prefix} MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 install

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* MANIFEST README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz MANIFEST.gz
%attr(755,root,root) %{_bindir}/di
%attr(644,root,root) %{_mandir}/man1/di.*
