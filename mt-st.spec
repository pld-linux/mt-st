Summary:	Programs to control tape device operations.
Summary(de):	Steuerung des magnetischen Bandlaufwerks (mt) 
Summary(fr):	Contrôle les opérations du lecteur de bandes magnétiques (mt)
Summary(tr):	Manyetik teyp sürücüsünün iþlevsel kontrolü (mt)
Name:		mt-st
Version:	0.5b
Release:	4
License:	BSD
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source0:	ftp://metalab.unc.edu/pub/Linux/system/backup/%{name}-%{version}.tar.gz
Patch0:		mt-st-buildroot.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		/bin
%define		_sbindir	/sbin

%description
The mt-st package contains the mt and st tape drive management
programs. Mt (for magnetic tape drives) and st (for SCSI tape devices)
can control rewinding, ejecting, skipping files and blocks and more.

This package can help you manage tape drives.

%description -l de
Das mt-Programm kann zur Erledigung von vielen Vorgängen auf Bändern
benutzt werden, etwa Rückspulen, Auswerfen, Überspringen von Dateien
und Blöcken usw.

%description -l fr
Le programme mt peut servir à réaliser de nombreuses opérations sur
les bandes, comme le rembobinage, l'éjection, le saut de fichiers et
de blocs, etc.

%description -l tr
mt programý teypler üzerinde rewind, eject, dosya, blok atlamasý gibi
birçok iþlemin gerçekleþtirilmesinde kullanýlabilir.

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
%attr(755,root,root) %{_bindir}/mt
%attr(755,root,root) %{_sbindir}/stinit
%{_mandir}/man1/mt.1*
%{_mandir}/man8/stinit.8*
