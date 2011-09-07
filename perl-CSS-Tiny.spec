Name:           perl-CSS-Tiny
Version:        1.15
Release:        4%{?dist}
Summary:        Read/Write .css files with as little code as possible

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/CSS-Tiny/
Source0:        http://www.cpan.org/authors/id/A/AD/ADAMK/CSS-Tiny-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(Clone)
BuildRequires:  perl(Test::Pod) >= 1.00
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Clone)

%description
CSS::Tiny is a perl class to read and write .css stylesheets with as
little code as possible, reducing load time and memory overhead.


%prep
%setup -q -n CSS-Tiny-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorlib}/CSS/
%{_mandir}/man3/*.3pm*


%changelog
* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1.15-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Oct 26 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.15-1
- update to 1.15

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.14-3
- Rebuild for perl 5.10 (again)

* Sun Jan 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.14-2
- rebuild for new perl

* Mon Sep  4 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.14-1
- Update to 1.14.

* Sat May 13 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.11-1
- First build.
