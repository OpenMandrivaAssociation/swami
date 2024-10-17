Name:       swami
Version:    2.0.0
Release:    3
Summary:    Instrument patch editor for wavetable synths (sounfont)

%define lib_major       0
%define lib_name        %mklibname %{name} %{lib_major}
%define lib_name_devel  %mklibname %{name} -d

License:    GPL
Group:      Sound
URL:        https://swami.sourceforge.net
Source0:    http://prdownloads.sourceforge.net/swami/%{name}-%{version}.tar.gz
Requires:   fluidsynth
Requires:   %{lib_name} = %{EVRD}

BuildRequires:  intltool
BuildRequires:  gtk-doc
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(gtk+)
BuildRequires:  pkgconfig(gtksourceview-2.0)
BuildRequires:  pkgconfig(libgnomecanvasmm-2.6)
BuildRequires:  pkgconfig(libglade-2.0)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(pygobject-2.0)
BuildRequires:  pkgconfig(pygtk-2.0)
BuildRequires:  pkgconfig(libinstpatch-1.0)
BuildRequires:  pkgconfig(fftw3)

%description
Swami is an instrument patch file editor using SoundFont files that allows
you to create and distribute instruments from audio samples used for
composing music. It uses the fluidsynth software synthesizer, which has real
time effect control, support for modulators, and routable audio via Jack.
Swami requires the libinstpatch library containing tools for soundfont
editing.

#-----------------------------------
%package -n %{lib_name}

Summary:        Library for processing Music Instrument patch files
Group:          System/Libraries
Requires:       pygtk2.0
Requires:       libinstpatch

%description -n %{lib_name}
Dynamic library files needed by the swami instrument patch editor.

%files -n %{lib_name}
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/lib%{name}*.so.*
%{_libdir}/%{name}/*.so

#-----------------------------------
%package -n %{lib_name_devel}
Summary:        Swami development headers
Group:          Sound
Requires:       %{name} = %{EVRD}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{lib_name_devel}
Development files to build applications with swami headers.

%files -n %{lib_name_devel}
%doc %{_datadir}/gtk-doc/html/lib%{name}
%doc %{_datadir}/gtk-doc/html/%{name}gui
%dir %{_includedir}/%{name}/lib%{name}
%{_includedir}/%{name}/lib%{name}/*.h
%dir %{_includedir}/%{name}/%{name}gui
%{_includedir}/%{name}/%{name}gui/*.h
%{_libdir}/*.so
#-----------------------------------

%prep
%setup -q

%build
LDFLAGS="-lgmodule-2.0" %configure2_5x --enable-static=no
%make

%install
%makeinstall_std

desktop-file-install --add-category="X-MandrivaLinux-Multimedia-Sound;" \
                     --remove-category="Midi;" \
                     --remove-category="Music;" \
                     --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

mkdir -p %{buildroot}%{_datadir}/pixmaps/
cp %{name}.svg %{buildroot}%{_datadir}/pixmaps/

%ifarch x86_64
install -d %{buildroot}%{python_sitelib}
mv %{buildroot}%{_prefix}/%_lib/python%{python_version}/site-packages/* %{buildroot}%{python_sitelib}/
%endif


%files
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/%name
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/swami-2.glade
%dir %{_datadir}/%{name}/images
%{_datadir}/%{name}/images/*.png
%{_datadir}/%{name}/images/knob.svg
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/icons/hicolor/48x48/apps/swami.png
%{_datadir}/icons/hicolor/scalable/apps/swami.svg
%{_datadir}/pygtk/2.0/defs/*.defs
%{python_sitelib}/*


