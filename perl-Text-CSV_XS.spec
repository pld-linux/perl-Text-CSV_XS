%include	/usr/lib/rpm/macros.perl
Summary:	Text-CSV_XS perl module
Summary(pl):	Modu³ perla Text-CSV_XS
Name:		perl-Text-CSV_XS
Version:	0.20
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/Text-CSV_XS-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
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
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/Text/CSV_XS/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Text/CSV_XS
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README}.gz

%{perl_sitearch}/Text/CSV_XS.pm

%dir %{perl_sitearch}/auto/Text/CSV_XS
%{perl_sitearch}/auto/Text/CSV_XS/.packlist
%{perl_sitearch}/auto/Text/CSV_XS/CSV_XS.bs
%attr(755,root,root) %{perl_sitearch}/auto/Text/CSV_XS/CSV_XS.so

%{_mandir}/man3/*
