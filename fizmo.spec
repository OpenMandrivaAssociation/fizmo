%define name    fizmo
%define version 0.6.3
%define release %mkrel 1

Name:           %{name}
Summary:        A Z-Machine interpreter supporting unicode, sound, blorbfile and more
Version:        %{version}
Release:        %{release}
URL:            http://spellbreaker.org/~chrender/fizmo/ 
Source0:        http://spellbreaker.org/~chrender/fizmo/fizmo-0.6.3.tar.gz
Patch0:		fizmo-0.6.3-config-mk.patch	
License:        BSD
Group:          Games/Other
BuildRequires:  libncursesw-devel libxml2-devel libSDL_sound-devel libsndfile-devel
BuildRoot:      %{_tmppath}/%{name}-buildroot

%description
Fizmo is a Z-Machine interpreter. That means it allows you to play interactive 
fiction, also know as textadventures, which where implemented either by Infocom
or created using the Inform compiler. It is a console-based interpreter, 
meaning that there is no graphical user interface, and works with all Z-machine
versions except version 6.
If you've never played a textadventure before, you might want to try 
"Mini-Zork" to get an idea what interactive fiction is about.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .mdv

%build
cp config.default.mk config.mk
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc CHANGELOG.txt COPYRIGHT.txt README.txt
%{_mandir}/*/*
%{_gamesbindir}/*
