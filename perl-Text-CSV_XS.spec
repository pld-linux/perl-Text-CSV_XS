%include	/usr/lib/rpm/macros.perl
Summary:	Text-CSV_XS perl module
Summary(pl):	Modu³ perla Text-CSV_XS
Name:		perl-Text-CSV_XS
Version:	0.23
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/Text-CSV_XS-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text-CSV_XS - comma-separated values manipulation routines.

%description -l pl
Text-CSV_XS umo¿liwia manipulowanie warto¶ciami rozdzielonymi
przecinkiem.

%prep
%setup -q -n Text-CSV_XS-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/Text/CSV_XS.pm
%dir %{perl_sitearch}/auto/Text/CSV_XS
%{perl_sitearch}/auto/Text/CSV_XS/CSV_XS.bs
%attr(755,root,root) %{perl_sitearch}/auto/Text/CSV_XS/CSV_XS.so
%{_mandir}/man3/*
