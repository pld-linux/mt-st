Summary:	Programs to control tape device operations
Summary(de):	Programme zum Kontrollieren von Streamern
Summary(fr):	Contrôle les opérations du lecteur de bandes magnétiques (mt)
Summary(pl):	Program do kontroli napêdów ta¶mowych
Summary(tr):	Manyetik teyp sürücüsünün iþlevsel kontrolü (mt)
Name:		mt-st
Version:	0.6
Release:	3
License:	BSD
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://metalab.unc.edu/pub/Linux/system/backup/%{name}-%{version}.tar.gz
Source1:	%{name}-non-english-man-pages.tar.bz2
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
Das mt-st-Paket enthält die mt und st Streamer-Management-Programme.
mt (für Magnetbandlaufwerke) und st (für SCSI-Streamer) können
Rückspulen, auswerfen, Dateien und blocks auslassen, und mehr.

%description -l fr
Le programme mt peut servir à réaliser de nombreuses opérations sur
les bandes, comme le rembobinage, l'éjection, le saut de fichiers et
de blocs, etc.

%description -l pl
Pakiet mt-st zawiera programy mt i st s³u¿±ce do kontroli napêdów
ta¶mowych. Mt (generalnie do napêdów ta¶mowych) i st (do napêdów
ta¶mowych SCSI) umo¿liwiaj± przewijanie, przesuwanie ta¶my i
wyjmowanie z napêdu kaset z tasm±.

%description -l tr
mt programý teypler üzerinde rewind, eject, dosya, blok atlamasý gibi
birçok iþlemin gerçekleþtirilmesinde kullanýlabilir.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT/%{_mandir}

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
%lang(es) %{_mandir}/es/man1/mt.1*
%lang(ja) %{_mandir}/ja/man1/mt.1*
%lang(pl) %{_mandir}/pl/man1/mt.1*
%{_mandir}/man8/stinit.8*
