Summary:	Programs to control tape device operations
Summary(de.UTF-8):   Programme zum Kontrollieren von Streamern
Summary(es.UTF-8):   Controla la operación de drivers de cinta magnética (mt)
Summary(fr.UTF-8):   Contrôle les opérations du lecteur de bandes magnétiques (mt)
Summary(pl.UTF-8):   Program do kontroli napędów taśmowych
Summary(pt_BR.UTF-8):   Controla a operação de drivers de fita magnética (mt)
Summary(ru.UTF-8):   Программы управления работой накопителей на магнитной ленте (mt)
Summary(tr.UTF-8):   Manyetik teyp sürücüsünün işlevsel kontrolü (mt)
Summary(uk.UTF-8):   Програми управління роботою накопичувачів на магнітній стрічці (mt)
Name:		mt-st
Version:	0.9b
Release:	1
License:	BSD
Group:		Applications/System
Source0:	ftp://metalab.unc.edu/pub/Linux/system/backup/%{name}-%{version}.tar.gz
# Source0-md5:	c80e992a8d16def7af7421549b26ce77
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	c2a75e15c360e4c8b2ef350cd6c2c45e
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-errno.h.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		/bin
%define		_sbindir	/sbin

%description
The mt-st package contains tape drive management programs, which can
control rewinding, ejecting, skipping files and blocks and more.

%description -l de.UTF-8
Das mt-st-Paket enthält die mt und st Streamer-Management-Programme.
mt (für Magnetbandlaufwerke) und st (für SCSI-Streamer) können
Rückspulen, auswerfen, Dateien und blocks auslassen, und mehr.

%description -l es.UTF-8
El programa mt puede ser usado para desarrollar varias operaciones en
cintas, incluyendo retroceder, expulsar, saltar archivos y bloques,
etc.

%description -l fr.UTF-8
Le programme mt peut servir à réaliser de nombreuses opérations sur
les bandes, comme le rembobinage, l'éjection, le saut de fichiers et
de blocs, etc.

%description -l pl.UTF-8
Pakiet mt-st zawiera programy służące do kontroli napędów taśmowych i
umożliwiające przewijanie, przesuwanie taśmy i wyjmowanie z napędu
kaset z taśmą.

%description -l pt_BR.UTF-8
O programa mt pode ser usado para desenvolver várias operações em
fitas, incluindo retroceder, ejetar, pular arquivos e blocos, etc.

%description -l ru.UTF-8
Пакет mt-st содержит программы управления лентами mt и st. Они могут
управлять перемоткой, выталкиванием ленты, пропуском файлов и блоков и
т.п.

%description -l tr.UTF-8
mt programı teypler üzerinde rewind, eject, dosya, blok atlaması gibi
birçok işlemin gerçekleştirilmesinde kullanılabilir.

%description -l uk.UTF-8
Пакет mt-st містить програми управління стрічками mt та st. Вони
можуть управляти перемоткою, виштовхуванням стрічки, пропуском файлів
та блоків та інше.


%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.stinit mt-st-*.lsm
%config(noreplace) %{_sysconfdir}/stinit.def
%attr(755,root,root) %{_bindir}/mt
%attr(755,root,root) %{_sbindir}/stinit
%{_mandir}/man1/mt.1*
%lang(es) %{_mandir}/es/man1/mt.1*
%lang(ja) %{_mandir}/ja/man1/mt.1*
%lang(pl) %{_mandir}/pl/man1/mt.1*
%{_mandir}/man8/stinit.8*
