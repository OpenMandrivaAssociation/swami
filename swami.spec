%define name	swami
%define version	0.9.4
%define release	%mkrel 4

Summary:	A GPL sound font editor
Name:		%{name}
Version:	%{version}
Release:	%{release}
License: 	GPLv2+
Group: 		Sound
URL: 		http://swami.sourceforge.net
Source0: 	%{name}-%{version}.tar.bz2
Source1:	%{name}16.png
Source2:	%{name}32.png
Source3:	%{name}48.png
Requires:	fluidsynth
BuildRequires:	fluidsynth-devel
BuildRequires:	libaudiofile-devel
BuildRequires:	libsndfile-devel
BuildRequires:	gtk-devel
BuildRequires:	zlib-devel
BuildRequires:	popt-devel
BuildRequires:	gettext
BuildRequires:	bison
BuildRoot: 	%_tmppath/%{name}-root

%description
Swami is an instrument patch file editor using SoundFont files that allows
you to create and distribute instruments from audio samples used for
composing music. It uses iiwusynth, a software synthesizer, which has real
time effect control, support for modulators, and routable audio via Jack.
This project supersedes the Smurf Sound Font Editor, and is an entire
object-oriented rewrite of it. The supporting libraries are GUI-independent
and can be used in your own programs for doing SoundFont manipulation.

%prep
%setup -q

%build
%configure2_5x	--with-pic --with-gnu-ld --disable-nls --disable-gnome-canvas
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
%find_lang %name

# Mandriva Menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Swami
Comment=SoundFont Editor
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;Audio;Editor;
EOF

mkdir -p $RPM_BUILD_ROOT%{_miconsdir} $RPM_BUILD_ROOT%{_liconsdir} $RPM_BUILD_ROOT%{_iconsdir}
cat %{SOURCE1} > $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
cat %{SOURCE2} > $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
cat %{SOURCE3} > $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README ABOUT-NLS
%{_bindir}/%name
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%name.desktop
%{_libdir}/%{name}


