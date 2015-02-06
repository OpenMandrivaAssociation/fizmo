Name:		fizmo
Summary:	A Z-Machine interpreter supporting unicode, sound, blorbfile and more
Version:	0.6.10
Release:	3
License:	BSD
Group:		Games/Other
URL:		http://spellbreaker.org/~chrender/fizmo/ 
Source0:	http://spellbreaker.org/~chrender/fizmo/source/fizmo-%{version}.tar.gz
Patch0:		fizmo-0.6.3-config-mk.patch	
BuildRequires:	SDL_sound-devel
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(sndfile)

%description
Fizmo is a Z-Machine interpreter. That means it allows you to play interactive 
fiction, also know as textadventures, which were implemented either by Infocom
or created using the Inform compiler. It is a console-based interpreter, 
meaning that there is no graphical user interface, and works with all Z-machine
versions except version 6.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .mdv

%build
cp config.default.mk config.mk
%make

%install
%makeinstall_std

%files
%defattr(-,root,root,0755)
%doc CHANGELOG.txt COPYRIGHT.txt README.txt
%{_mandir}/*/*
%{_gamesbindir}/*


