%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	CSV_XS
Summary:	Text::CSV_XS perl module
Summary(pl):	Modu³ perla Text::CSV_XS
Name:		perl-Text-CSV_XS
Version:	0.23
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::CSV_XS - comma-separated values manipulation routines.

%description -l pl
Text::CSV_XS umo¿liwia manipulowanie warto¶ciami rozdzielonymi
przecinkiem.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_sitearch}/Text/CSV_XS.pm
%dir %{perl_sitearch}/auto/Text/CSV_XS
%{perl_sitearch}/auto/Text/CSV_XS/CSV_XS.bs
%attr(755,root,root) %{perl_sitearch}/auto/Text/CSV_XS/CSV_XS.so
%{_mandir}/man3/*
