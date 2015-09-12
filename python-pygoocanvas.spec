%define oname pygoocanvas
%define pycairo 1.8.4
%define _disable_rebuild_configure 1

Summary:	GooCanvas python bindings
Name:		python-%{oname}
Version:	0.14.1
Release:	14
License:	LGPLv2
Group:		Development/Python
Url:		http://developer.berlios.de/projects/pygoocanvas/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{oname}/%{oname}-%{version}.tar.bz2
Patch0:		0001-Check-the-return-value-of-PycairoContext_FromContext.patch
BuildRequires:	docbook-style-xsl
BuildRequires:	gnome-doc-utils
BuildRequires:	pkgconfig(goocanvas)
BuildRequires:	pkgconfig(pycairo) >= %{pycairo}
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	python2-devel

Requires:	python-cairo >= %{pycairo}
Provides:	%{oname} = %{version}-%{release}

%description
This package includes Python bindings for GooCanvas. It is
needed to run programs written in Python and using GooCanvas
set.

%package devel
Summary:	GooCanvas python bindings - Development files
Group:		Development/Python
Requires:	%{name} = %{version}-%{release}

%description devel
This package includes development files of python bindings for GooCanvas.

%prep
%setup -qn %{oname}-%{version}
%apply_patches

%build
ln -s %{_bindir}/python2 python
export PATH=`pwd`:$PATH

%configure
%make

%install
%makeinstall_std

%files
%doc %{_datadir}/gtk-doc/html/%{oname}
%{python2_sitearch}/*

%files devel
%{_libdir}/pkgconfig/*.pc

