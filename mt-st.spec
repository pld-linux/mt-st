Summary: Programs to control tape device operations.
Name: mt-st
Version: 0.5b
Release: 3
Copyright: BSD
Group: Applications/System
Source: ftp://metalab.unc.edu/pub/Linux/system/backup/mt-st-0.5b.tar.gz
Patch: mt-st-buildroot.patch
BuildRoot: /var/tmp/%{name}-root

%description
The mt-st package contains the mt and st tape drive management
programs. Mt (for magnetic tape drives) and st (for SCSI tape
devices) can control rewinding, ejecting, skipping files and
blocks and more.

This package can help you manage tape drives.

%prep
%setup -q
%patch -p1 -b .buildroot

%build
make CFLAGS="$RPM_OPT_FLAGS -Wall"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{bin,sbin,usr/man/man1,usr/man/man8}
make install

%files
%defattr(-,root,root)
%doc COPYING README README.stinit mt-st-0.5b.lsm stinit.def.examples
/bin/mt
/sbin/stinit
/usr/man/man1/mt.1
/usr/man/man8/stinit.8
