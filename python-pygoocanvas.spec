%define oname pygoocanvas
%define pycairo 1.8.4
Name: python-%{oname}
Summary: GooCanvas python bindings
Version: 0.14.1
Release: 5
URL: http://developer.berlios.de/projects/pygoocanvas/
License: LGPL
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: goocanvas-devel >= 0.14
BuildRequires: pygtk2.0-devel >= 2.10.4
BuildRequires: pkgconfig(pycairo) >= %pycairo
BuildRequires: gnome-doc-utils
BuildRequires: docbook-style-xsl
Requires: python-cairo >= %pycairo
Provides: %{oname} = %{version}-%{release}
Source: http://ftp.gnome.org/pub/GNOME/sources/%{oname}/%{oname}-%{version}.tar.bz2
Patch0: 0001-Check-the-return-value-of-PycairoContext_FromContext.patch

%description
This package includes Python bindings for GooCanvas. It is
needed to run programs written in Python and using GooCanvas
set.

%package devel
Summary: GooCanvas python bindings - Development files
Group: Development/Python
Requires: %name = %version

%description devel
This package includes development files of python bindings for GooCanvas.

%prep
%setup -q -n %{oname}-%{version}
%apply_patches

%build
%configure2_5x
%make

%install
rm -fr %{buildroot}
%makeinstall_std

%clean
rm -fr %{buildroot}

%files
%doc %{_datadir}/gtk-doc/html/%{oname}
%{python_sitearch}/*

%files devel
%{_libdir}/pkgconfig/*.pc


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.14.1-3mdv2011.0
+ Revision: 668026
- mass rebuild

* Mon Nov 15 2010 Maarten Vanraes <alien@mandriva.org> 0.14.1-2mdv2011.0
+ Revision: 597776
- fixes a major issue with dependant programs like pitivi

* Sun May 10 2009 Götz Waschk <waschk@mandriva.org> 0.14.1-1mdv2011.0
+ Revision: 374089
- new version
- bump deps

* Wed Mar 18 2009 Götz Waschk <waschk@mandriva.org> 0.14.0-1mdv2009.1
+ Revision: 357123
- update to new version 0.14.0

* Sat Dec 27 2008 Götz Waschk <waschk@mandriva.org> 0.13.1-1mdv2009.1
+ Revision: 319929
- update to new version 0.13.1

* Fri Dec 26 2008 Adam Williamson <awilliamson@mandriva.org> 0.13.0-2mdv2009.1
+ Revision: 319469
- rebuild with python 2.6

* Sun Nov 30 2008 Götz Waschk <waschk@mandriva.org> 0.13.0-1mdv2009.1
+ Revision: 308605
- new version
- bump deps

* Mon Sep 22 2008 Götz Waschk <waschk@mandriva.org> 0.12.0-1mdv2009.0
+ Revision: 286435
- new version
- new source URL

* Wed Jun 25 2008 Funda Wang <fwang@mandriva.org> 0.10.0-1mdv2009.0
+ Revision: 229067
- New version 0.10.0

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Mon Sep 03 2007 Adam Williamson <awilliamson@mandriva.org> 0.9.0-1mdv2008.0
+ Revision: 78462
- update goocanvas buildrequires version
- new release 0.9.0, rebuild against new libgoocanvas

* Wed Jul 25 2007 Funda Wang <fwang@mandriva.org> 0.8.0-1mdv2008.0
+ Revision: 55311
- BR docbook-style-xsl
- Bump release
- Fill the file list
- Import pygoocanvas
- Created package structure for python-pygoocanvas.

