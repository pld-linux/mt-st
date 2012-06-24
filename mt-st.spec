Summary:	Programs to control tape device operations.
Summary(de):	Steuerung des magnetischen Bandlaufwerks (mt) 
Summary(fr):	Contr�le les op�rations du lecteur de bandes magn�tiques (mt)
Summary(tr):	Manyetik teyp s�r�c�s�n�n i�levsel kontrol� (mt)
Name:		mt-st
Version:	0.5b
Release:	4
License:	BSD
Group:		Utilities/System
Group(pl):	Narz�dzia/System
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
Das mt-Programm kann zur Erledigung von vielen Vorg�ngen auf B�ndern
benutzt werden, etwa R�ckspulen, Auswerfen, �berspringen von Dateien
und Bl�cken usw.

%description -l fr
Le programme mt peut servir � r�aliser de nombreuses op�rations sur
les bandes, comme le rembobinage, l'�jection, le saut de fichiers et
de blocs, etc.

%description -l tr
mt program� teypler �zerinde rewind, eject, dosya, blok atlamas� gibi
bir�ok i�lemin ger�ekle�tirilmesinde kullan�labilir.

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
