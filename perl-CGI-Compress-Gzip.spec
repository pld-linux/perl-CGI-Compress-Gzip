#
# Conditional build:
%bcond_without	tests	# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	CGI
%define		pnam	Compress-Gzip
Summary:	CGI::Compress::Gzip - CGI with automatically compressed output
Summary(pl.UTF-8):	CGI::Compress::Gzip - CGI z automatycznie kompresowanym wyjściem
Name:		perl-CGI-Compress-Gzip
Version:	0.21
Release:	1
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tgz
# Source0-md5:	b24f4421b0d681c6078132f0cd7e524e
BuildRequires:	perl-IO-Zlib
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::Compress::Gzip extends the CGI class to auto-detect whether the
client browser wants compressed output and, if so and if the script
chooses HTML output, apply gzip compression on any content header for
STDOUT. This module is intended to be a drop-in replacement for CGI.pm
in a typical scripting environment.

%description -l pl.UTF-8
CGI::Compress::Gzip rozszerza klasę CGI o automatyczne wykrywanie czy
przeglądarka chce wyjście w postaci skompresowanej i jeśli tak oraz
skrypt wybierze wyjście HTML, aplikowanie kompresji gzip do dowolnych
nagłówków na standardowym wyjściu. Ten moduł jest robiony z myślą, by
był zamiennikiem CGI.pm w typowym środowisku skryptowym.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README index.html
%dir %{perl_vendorlib}/CGI/Compress
%{perl_vendorlib}/CGI/Compress/Gzip.pm
%dir %{perl_vendorlib}/CGI/Compress/Gzip
%{perl_vendorlib}/CGI/Compress/Gzip/FileHandle.pm
%{_mandir}/man3/*
