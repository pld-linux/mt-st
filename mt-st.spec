Summary:	Programs to control tape device operations.
Name:		mt-st
Version:	0.5b
Release:	4
Copyright:	BSD
Group:		Applications/System
Source:		ftp://metalab.unc.edu/pub/Linux/system/backup/%{name}-%{version}.tar.gz
Patch:		mt-st-buildroot.patch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
The mt-st package contains the mt and st tape drive management
programs. Mt (for magnetic tape drives) and st (for SCSI tape
devices) can control rewinding, ejecting, skipping files and
blocks and more.

This package can help you manage tape drives.

%prep
%setup -q
%patch -p1

%build
make CFLAGS="$RPM_OPT_FLAGS -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{bin,sbin,%{_mandir}/man{1,8}}
make install

gzip -9nf README README.stinit mt-st-0.5b.lsm stinit.def.examples \
	$RPM_BUILD_ROOT%{_mandir}/man{1,8}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,README.stinit,mt-st-0.5b.lsm,stinit.def.examples}.gz
%attr(755,root,root) /bin/mt
%attr(755,root,root) /sbin/stinit
%{_mandir}/man1/mt.1.gz
%{_mandir}/man8/stinit.8.gz
