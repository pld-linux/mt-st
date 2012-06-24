Summary:	Programs to control tape device operations
Summary(de):	Programme zum Kontrollieren von Streamern
Summary(es):	Controla la operaci�n de drivers de cinta magn�tica (mt)
Summary(fr):	Contr�le les op�rations du lecteur de bandes magn�tiques (mt)
Summary(pl):	Program do kontroli nap�d�w ta�mowych
Summary(pt_BR):	Controla a opera��o de drivers de fita magn�tica (mt)
Summary(ru):	��������� ���������� ������� ����������� �� ��������� ����� (mt)
Summary(tr):	Manyetik teyp s�r�c�s�n�n i�levsel kontrol� (mt)
Summary(uk):	�������� �����̦��� ������� ����������ަ� �� ���Φ�Φ� ��Ҧ�æ (mt)
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
Das mt-st-Paket enth�lt die mt und st Streamer-Management-Programme.
mt (f�r Magnetbandlaufwerke) und st (f�r SCSI-Streamer) k�nnen
R�ckspulen, auswerfen, Dateien und blocks auslassen, und mehr.

%description -l es
El programa mt puede ser usado para desarrollar varias operaciones
en cintas, incluyendo retroceder, expulsar, saltar archivos y
bloques, etc.

%description -l fr
Le programme mt peut servir � r�aliser de nombreuses op�rations sur
les bandes, comme le rembobinage, l'�jection, le saut de fichiers et
de blocs, etc.

%description -l pl
Pakiet mt-st zawiera programy s�u��ce do kontroli nap�d�w
ta�mowych i umo�liwiaj�ce przewijanie, przesuwanie ta�my i
wyjmowanie z nap�du kaset z tasm�.

%description -l pt_BR
O programa mt pode ser usado para desenvolver v�rias opera��es em
fitas, incluindo retroceder, ejetar, pular arquivos e blocos, etc.

%description -l ru
����� mt-st �������� ��������� ���������� ������� mt � st.
��� ����� ��������� ����������, ������������� �����,
��������� ������ � ������ � �.�.

%description -l tr
mt program� teypler �zerinde rewind, eject, dosya, blok atlamas� gibi
bir�ok i�lemin ger�ekle�tirilmesinde kullan�labilir.

%description -l uk
����� mt-st ͦ����� �������� �����̦��� ��Ҧ����� mt �� st.
���� ������ ��������� ����������, �������������� ��Ҧ���,
��������� ���̦� �� ���˦� �� ����.


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
