%define oname pygoocanvas

Name: python-%{oname}
Summary: GooCanvas python bindings
Version: 0.13.0
Release: %mkrel 1
URL: http://developer.berlios.de/projects/pygoocanvas/
License: LGPL
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: goocanvas-devel >= 0.13
BuildRequires: pygtk2.0-devel >= 2.10.4
BuildRequires: gnome-doc-utils
BuildRequires: docbook-style-xsl
Provides: %{oname} = %{version}-%{release}
Source: http://ftp.gnome.org/pub/GNOME/sources/%{oname}/%{oname}-%{version}.tar.bz2

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
