#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	CSV_XS
Summary:	Text::CSV_XS perl module
Summary(pl.UTF-8):	Moduł perla Text::CSV_XS
Name:		perl-Text-CSV_XS
Version:	0.32
Release:	2
# same as perl
License:	GPL v1+ oe Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Text/%{pdir}-%{pnam}-%{version}.tgz
# Source0-md5:	ad96b60f2dd1fdb97763b4db8e08209e
URL:		http://search.cpan.org/dist/Text-CSV_XS/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::CSV_XS - comma-separated values manipulation routines.

%description -l pl.UTF-8
Text::CSV_XS umożliwia manipulowanie wartościami rozdzielonymi
przecinkiem.

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

%{__make} \
	CC="%{__cc}" \
	install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorarch}/Text/CSV_XS.pm
%dir %{perl_vendorarch}/auto/Text/CSV_XS
%{perl_vendorarch}/auto/Text/CSV_XS/CSV_XS.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Text/CSV_XS/CSV_XS.so
%{_mandir}/man3/*
