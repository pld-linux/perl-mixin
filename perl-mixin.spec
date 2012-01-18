#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	mixin
Summary:	mixin - mix-in inheritance, an alternative to multiple inheritance
Summary(pl.UTF-8):	mixin - dziedziczenie "towarzyskie", alternatywa dla dziedziczenia wielokrotnego
Name:		perl-mixin
Version:	0.07
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/MS/MSCHWERN/%{pdir}-%{version}.tar.gz
# Source0-md5:	2b764a8c29f50a3af0f8e8c24fa7b582
URL:		http://search.cpan.org/dist/mixin/
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

%description -l pl.UTF-8
Dziedziczenie "mixin" (towarzyskie) jest alternatywą dla zwykłego
dziedziczenia wielokrotnego i rozwiązuje problem braku wiedzy o tym,
który z przodków zostanie wywołany. Rozwiązuje ono również kilka
innych podstępnych problemów, jak na przykład dziedziczenie rombowe.

Idea polega na tym, by rozwiązać problemy, które rozwiązuje
dziedziczenie wielokrotne bez problemów dziedziczenia wielokrotnego.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Build.PL \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install \
	destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/*.pm
%{perl_vendorlib}/mixin/
%{_mandir}/man3/*
