Name:       swami
Version:    2.0.0
Release:    1
Summary:    Instrument patch editor for wavetable synths (sounfont)

%define lib_major       0
%define lib_name        %mklibname %{name} %{lib_major}
%define lib_name_devel  %mklibname %{name} -d

License:    GPL
Group:      Sound
URL:        http://swami.sourceforge.net
Source0:    http://prdownloads.sourceforge.net/swami/%{name}-%{version}.tar.gz
Requires:   fluidsynth
Requires:   %{lib_name}

BuildRequires:  intltool
BuildRequires:  gtk-doc
BuildRequires:  fluidsynth-devel
BuildRequires:  sndfile-devel
BuildRequires:  gtk+-devel
BuildRequires:  gtksourceview-devel
BuildRequires:  libgnomecanvasmm-devel
BuildRequires:  libglade2.0-devel
BuildRequires:  librsvg2-devel
BuildRequires:  python-gobject-devel
BuildRequires:  pygtk2.0-devel
BuildRequires:  instpatch-devel
BuildRequires:  fftw3-devel
BuildRoot:      %_tmppath/%{name}-root

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
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/lib%{name}*.so.*
%{_libdir}/%{name}/*.so

#-----------------------------------
%package -n %{lib_name_devel}
Summary:        Swami development headers
Group:          Sound
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{lib_name_devel}
Development files to build applications with swami headers.

%files -n %{lib_name_devel}
%defattr(-,root,root,-)
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
rm -rf %{buildroot}
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

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
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


%changelog
* Mon Nov 01 2010 Frank Kober <emuse@mandriva.org> 2.0.0-1mdv2011.0
+ Revision: 591471
- revert configure macro
- add missing BR, do not use configure macro
- new version 2.0.0
- new version 2.0.0

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 0.9.4-5mdv2009.0
+ Revision: 261302
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.9.4-4mdv2009.0
+ Revision: 253849
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sat Jan 26 2008 Funda Wang <fwang@mandriva.org> 0.9.4-2mdv2008.1
+ Revision: 158224
- fix menu entry

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.9.4-1mdv2008.1
+ Revision: 140904
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Sun Jan 07 2007 Crispin Boylan <crisb@mandriva.org> 0.9.4-1mdv2007.0
+ Revision: 105338
- BuildRequires popt-devel
- New version, XDG menu
- Import swami

* Mon May 01 2006 Austin Acton <austin@mandriva.org> 0.9.3-1mdk
- New release 0.9.3

* Sun Feb 06 2005 Austin Acton <austin@mandrake.org> 0.9.2-2mdk
- birthday
- fix summary and buildrequires

