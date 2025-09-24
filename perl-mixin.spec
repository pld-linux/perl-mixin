#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	mixin
Summary:	mixin - mix-in inheritance, an alternative to multiple inheritance
Summary(pl.UTF-8):	mixin - dziedziczenie "towarzyskie", alternatywa dla dziedziczenia wielokrotnego
Name:		perl-mixin
Version:	0.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-authors/id/S/SH/SHLOMIF/%{pdir}-%{version}.tar.gz
# Source0-md5:	564aef117caca4a000f33700711d18a3
URL:		https://metacpan.org/dist/mixin
BuildRequires:	perl-Module-Build >= 0.36
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Test-NoWarnings
BuildRequires:	perl-Test-Simple >= 0.40
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
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
%{perl_vendorlib}/mixin.pm
%{perl_vendorlib}/mixin
%{_mandir}/man3/mixin.3pm*
%{_mandir}/man3/mixin::with.3pm*
