
# Conditional build:
%bcond_without	tests	# do perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	CGI
%define pnam	Compress-Gzip
Summary:	CGI::Compress::Gzip - CGI with automatically compressed output
Name:		perl-CGI-Compress-Gzip
Version:	0.17
Release:	1
# same as perl
License:	GPL or Commercial
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tgz
# Source0-md5:	6bea0617aa8ea5e0040817fe0bcc28d5
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::Compress::Gzip extends the CGI class to auto-detect whether the client browser wants compressed output and, if so
and if the script chooses HTML output, apply gzip compression on any content header for STDOUT.  This module is intended
to be a drop-in replacement for CGI.pm in a typical scripting environment.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:make test}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/CGI/Compress/Gzip.pm
%{_mandir}/man3/*
