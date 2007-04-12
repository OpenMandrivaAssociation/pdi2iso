%define name	pdi2iso
%define version	0.1
%define release	%mkrel 3

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


