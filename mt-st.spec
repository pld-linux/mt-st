Summary:	Programs to control tape device operations
Summary(de):	Programme zum Kontrollieren von Streamern
Summary(es):	Controla la operaciСn de drivers de cinta magnИtica (mt)
Summary(fr):	ContrТle les opИrations du lecteur de bandes magnИtiques (mt)
Summary(pl):	Program do kontroli napЙdСw ta╤mowych
Summary(pt_BR):	Controla a operaГЦo de drivers de fita magnИtica (mt)
Summary(ru):	Программы управления работой накопителей на магнитной ленте (mt)
Summary(tr):	Manyetik teyp sЭrЭcЭsЭnЭn iЧlevsel kontrolЭ (mt)
Summary(uk):	Програми управл╕ння роботою накопичувач╕в на магн╕тн╕й стр╕чц╕ (mt)
Name:		mt-st
Version:	0.7
Release:	3
License:	BSD
Group:		Applications/System
Source0:	ftp://metalab.unc.edu/pub/Linux/system/backup/%{name}-%{version}.tar.gz
# Source0-md5:	3e1cb5a09dc73c6e54089e2056f9ff55
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	c2a75e15c360e4c8b2ef350cd6c2c45e
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-errno.h.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		/bin
%define		_sbindir	/sbin

%description
The mt-st package contains tape drive management
programs, which can control rewinding, ejecting, skipping files and blocks and more.

%description -l de
Das mt-st-Paket enthДlt die mt und st Streamer-Management-Programme.
mt (fЭr Magnetbandlaufwerke) und st (fЭr SCSI-Streamer) kЖnnen
RЭckspulen, auswerfen, Dateien und blocks auslassen, und mehr.

%description -l es
El programa mt puede ser usado para desarrollar varias operaciones
en cintas, incluyendo retroceder, expulsar, saltar archivos y
bloques, etc.

%description -l fr
Le programme mt peut servir Ю rИaliser de nombreuses opИrations sur
les bandes, comme le rembobinage, l'Иjection, le saut de fichiers et
de blocs, etc.

%description -l pl
Pakiet mt-st zawiera programy sЁu©╠ce do kontroli napЙdСw
ta╤mowych i umo©liwiaj╠ce przewijanie, przesuwanie ta╤my i
wyjmowanie z napЙdu kaset z tasm╠.

%description -l pt_BR
O programa mt pode ser usado para desenvolver vАrias operaГУes em
fitas, incluindo retroceder, ejetar, pular arquivos e blocos, etc.

%description -l ru
Пакет mt-st содержит программы управления лентами mt и st.
Они могут управлять перемоткой, выталкиванием ленты,
пропуском файлов и блоков и т.п.

%description -l tr
mt programЩ teypler Эzerinde rewind, eject, dosya, blok atlamasЩ gibi
birГok iЧlemin gerГekleЧtirilmesinde kullanЩlabilir.

%description -l uk
Пакет mt-st м╕стить програми управл╕ння стр╕чками mt та st.
Вони можуть управляти перемоткою, виштовхуванням стр╕чки,
пропуском файл╕в та блок╕в та ╕нше.


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
