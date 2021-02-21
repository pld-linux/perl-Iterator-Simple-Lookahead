#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Iterator
%define		pnam	Simple-Lookahead
Summary:	Iterator::Simple::Lookahead Perl module
Summary(pl.UTF-8):	Moduł Perla Iterator::Simple::Lookahead
Name:		perl-Iterator-Simple-Lookahead
Version:	0.09
Release:	1
License:	Perl5
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Iterator/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1620abf6f4442ee472fc8fdcd7b02be9
URL:		https://metacpan.org/release/Iterator-Simple-Lookahead
BuildRequires:	perl-Class-Accessor
BuildRequires:	perl-Iterator-Simple
BuildRequires:	perl-Module-Install
BuildRequires:	perl-devel >= 1:5.10.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Iterator::Simple::Lookahead Perl module.

%description -l pl.UTF-8
Moduł Perla Iterator::Simple::Lookahead.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} -j1

%{?with_tests:%{__make} -j1 test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Iterator/Simple
%{perl_vendorlib}/Iterator/Simple/Lookahead.pm
%{_mandir}/man3/Iterator::Simple::Lookahead.3pm*
