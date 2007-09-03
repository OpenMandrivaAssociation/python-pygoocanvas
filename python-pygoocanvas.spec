%define oname pygoocanvas

Name: python-pygoocanvas
Summary: GooCanvas python bindings
Version: 0.9.0
Release: %mkrel 1
URL: http://developer.berlios.de/projects/pygoocanvas/
License: LGPL
Group: Development/Python
BuildRequires: goocanvas-devel >= 0.9
BuildRequires: pygtk2.0-devel >= 2.10.4
BuildRequires: gnome-doc-utils
BuildRequires: docbook-style-xsl
Provides: %{oname} = %{version}-%{release}
Source: %{oname}-%{version}.tar.gz

%description
This package include Python bindings for GooCanvas. It is
needed to run programs written in Python and using GooCanvas
set.

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

