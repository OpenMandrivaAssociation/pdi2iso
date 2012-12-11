%define name	pdi2iso
%define version	0.1
%define release	%mkrel 6

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Instant Copy CD Images to ISO
Source:		%{name}-%{version}.tar.bz2
URL:		http://developer.berlios.de/projects/pdi2iso/
License:	GPL
Group:		Archiving/Other
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description 
PDI2ISO is a very simple utility to convert an instant copy bin image
to the standard ISO-9660 format.

%prep
%setup -q

%build
gcc %optflags ./src/pdi2iso.c -o pdi2iso

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install pdi2iso %{buildroot}%{_bindir}/pdi2iso

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGELOG
%{_bindir}/pdi2iso




%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.1-6mdv2010.0
+ Revision: 430250
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.1-5mdv2009.0
+ Revision: 255172
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.1-3mdv2008.1
+ Revision: 136654
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Mar 30 2007 Olivier Blin <oblin@mandriva.com> 0.1-3mdv2007.1
+ Revision: 149958
- rebuild because of binary package loss
- Import pdi2iso

* Tue May 02 2006 Olivier Thauvin <nanardon@mandriva.org> 0.1-2mdk
- Birthday Rebuild

* Fri Apr 01 2005 Olivier Thauvin <nanardon@mandrake.org> 0.1-1mdk
- from Michael Berger <webmaster@hmb-linux.de>
  - 0.1

