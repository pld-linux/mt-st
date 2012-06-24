Summary:	Programs to control tape device operations
Summary(de):	Programme zum Kontrollieren von Streamern
Summary(fr):	Contr�le les op�rations du lecteur de bandes magn�tiques (mt)
Summary(pl):	Program do kontroli nap�d�w ta�mowych
Summary(tr):	Manyetik teyp s�r�c�s�n�n i�levsel kontrol� (mt)
Name:		mt-st
Version:	0.6
Release:	1
License:	BSD
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://metalab.unc.edu/pub/Linux/system/backup/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-errno.h.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		/bin
%define		_sbindir	/sbin

%description
The mt-st package contains the mt and st tape drive management
programs. Mt (for magnetic tape drives) and st (for SCSI tape devices)
can control rewinding, ejecting, skipping files and blocks and more.

%description -l de
Das mt-st-Paket enth�lt die mt und st Streamer-Management-Programme.
mt (f�r Magnetbandlaufwerke) und st (f�r SCSI-Streamer) k�nnen
R�ckspulen, auswerfen, Dateien und blocks auslassen, und mehr.

%description -l fr
Le programme mt peut servir � r�aliser de nombreuses op�rations sur
les bandes, comme le rembobinage, l'�jection, le saut de fichiers et
de blocs, etc.

%description -l pl
Pakiet mt-st zawiera programy mt i st s�u��ce do kontroli nap�d�w
ta�mowych. Mt (generalnie do nap�d�w ta�mowych) i st (do nap�d�w
ta�mowych SCSI) umo�liwiaj� przewijanie, przesuwanie ta�my i
wyjmowanie z nap�du kaset z tasm�.

%description -l tr
mt program� teypler �zerinde rewind, eject, dosya, blok atlamas� gibi
bir�ok i�lemin ger�ekle�tirilmesinde kullan�labilir.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} CFLAGS="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS} -Wall"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README README.stinit mt-st-*.lsm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%config(noreplace) %{_sysconfdir}/stinit.def
%attr(755,root,root) %{_bindir}/mt
%attr(755,root,root) %{_sbindir}/stinit
%{_mandir}/man1/mt.1*
%{_mandir}/man8/stinit.8*
