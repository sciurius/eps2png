# -*- rpm-spec -*-

Name: eps2png
Version: 2.903
Release: 1
Source: https://github.com/sciurius/eps2png/archive/%{name}-%{version}.tar.gz
BuildArch: noarch
URL: https://johan.vromans.org/software/sw_eps2png.html
Vendor: Squirrel Consultancy
Summary: Converter from EPS to PNG, JPG and GIF
License: GPL+ or Artistic
Group: Applications/Graphics

Requires: perl >= 5.010001
Requires: ghostscript
Requires: netpbm-progs
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.5503
BuildRequires: ghostscript
BuildRequires: netpbm-progs

%description
Converts files from EPS format (Encapsulated PostScript) to some
popular image formats.

Note that Ghostcript is required for the actual conversion.

GIF support has been removed from modern Ghostscript. If you want GIF
format eps2png will convert to an intermediate format and call netPBM
tool ppmtogif for the actual conversion.

%prep
%setup -q -n %{name}-%{version}

%build
%{__perl} Makefile.PL OPTIMIZE="$RPM_OPT_FLAGS" INSTALLDIRS=site INSTALLSITEBIN=%{_bindir} INSTALLSITESCRIPT=%{_bindir} INSTALLSITEMAN1DIR=%{_mandir}/man1 INSTALLSITEMAN3DIR=%{_mandir}/man3 INSTALLSCRIPT=%{_bindir}
make %{?_smp_mflags}

%check
if [ -z "$RPMBUILD_NOTESTS" ]; then
   make test
fi

%install
rm -rf $RPM_BUILD_ROOT
%{__mkdir} -p $RPM_BUILD_ROOT%{_bindir}
%{__mkdir} -p $RPM_BUILD_ROOT%{_mandir}/man1
%{__install} -m 0755 script/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
%{__install} -m 0644 blib/man1/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*

%changelog
* Mon Jan  6 2020 Johan Vromans <jvromans@squirrel.nl> - 2.903-1
- Upgrade to upstream.

* Thu Mar 27 2008 Johan Vromans <jvromans@squirrel.nl> - 1.1-1
- Initial version.
