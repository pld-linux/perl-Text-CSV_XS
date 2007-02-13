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
Version:	0.23
Release:	5
# same as perl
License:	GPL v1+ oe Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	936eca163a09e92353565ad37ee7a4fa
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
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
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} \
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
