%define	pdir	Text
%define	pnam	CSV_XS
%include	/usr/lib/rpm/macros.perl
Summary:	Text-CSV_XS perl module
Summary(pl):	Modu� perla Text-CSV_XS
Name:		perl-Text-CSV_XS
Version:	0.23
Release:	2

License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text-CSV_XS - comma-separated values manipulation routines.

%description -l pl
Text-CSV_XS umo�liwia manipulowanie warto�ciami rozdzielonymi
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
