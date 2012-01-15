#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	CSV_XS
Summary:	Text::CSV_XS - comma-separated values manipulation routines
Summary(pl.UTF-8):	Text::CSV_XS - operacje na wartościach oddzielonych przecinkami
Name:		perl-Text-CSV_XS
Version:	0.85
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Text/%{pdir}-%{pnam}-%{version}.tgz
# Source0-md5:	876e4017ef95eaa5740730fef14e976f
URL:		http://search.cpan.org/dist/Text-CSV_XS/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::CSV_XS Perl module provides facilities for the composition and
decomposition of comma-separated values. An instance of the
Text::CSV_XS class can combine fields into a CSV string and parse a
CSV string into fields.

%description -l pl.UTF-8
Moduł Perla Text::CSV_XS udostępnia metody do składania i rozkładania
wartości oddzielonych przecinkami. Instancja klasy Text::CSV_CS
potrafi łączyć pola w łańcuch CSV oraz rozkładać łańcuch CSV na pola.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorarch}/Text/CSV_XS.pm
%dir %{perl_vendorarch}/auto/Text/CSV_XS
%{perl_vendorarch}/auto/Text/CSV_XS/CSV_XS.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Text/CSV_XS/CSV_XS.so
%{_mandir}/man3/Text::CSV_XS.3pm*
