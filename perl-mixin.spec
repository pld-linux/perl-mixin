#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	mixin
Summary:	mixin - mix-in inheritance, an alternative to multiple inheritance
Summary(pl):	mixin - dziedziczenie "towarzyskie", alternatywa dla dziedziczenia wielokrotnego
Name:		perl-mixin
Version:	0.04
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/MS/MSCHWERN/%{pdir}-%{version}.tar.gz
# Source0-md5:	cc1932a0a90dd905726373d7c2f6377f
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mixin inheritance is an alternative to the usual multiple-inheritance
and solves the problem of knowing which parent will be called.
It also solves a number of tricky problems like diamond inheritence.

The idea is to solve the same sets of problems which MI solves without
the problems of MI.

%description -l pl
Dziedziczenie "mixin" (towarzyskie) jest alternatyw± dla zwyk³ego
dziedziczenia wielokrotnego i rozwi±zuje problem braku wiedzy o tym,
który z przodków zostanie wywo³any. Rozwi±zuje ono równie¿ kilka
innych podstêpnych problemów, jak na przyk³ad dziedziczenie rombowe.

Idea polega na tym, by rozwi±zaæ problemy, które rozwi±zuje
dziedziczenie wielokrotne bez problemów dziedziczenia wielokrotnego.

%prep
%setup -q -n %{pdir}-%{version}

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
%doc Changes
%{perl_vendorlib}/*.pm
%{perl_vendorlib}/mixin/
%{_mandir}/man3/*
