%define	name	geglmm
%define	version	0.1.0
%define	release	%mkrel 3

%define major	3
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Name:           %name
Version:        %version
Release:        %release
License:        LGPLv3
URL:		https://gegl.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gcc-c++
BuildRequires:  gegl-devel >= 0.1.0
BuildRequires:  babl-devel >= 0.1.0
BuildRequires:  glibmm2.4-devel
Source0:        http://ftp.gnome.org/pub/GNOME/sources/geglmm/%{name}-%{version}.tar.bz2
Group:          System/Libraries
Summary:        A graphic processing library, C++ bindings

%description
C++ binding for GEGL.
GEGL (Generic Graphics Library) is a graph based image processing framework.

%package -n %libname
Group:          System/Libraries
Summary:        A graphic processing library, C++ bindings

%description -n %libname
C++ binding for GEGL.
GEGL (Generic Graphics Library) is a graph based image processing framework.


%package -n %develname
Group:          Development/C++
Summary:        A graphic processing library, C++ bindings
Requires:       gegl-devel >= %{version}
Requires:       %{libname} = %{version}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %develname
C++ binding for GEGL.
GEGL (Generic Graphics Library) is a graph based image processing framework.
(Development files)


%prep
%setup -q 

%build
%configure2_5x
%make

%install
rm -rf "$RPM_BUILD_ROOT"
%makeinstall

%clean
rm -rf "$RPM_BUILD_ROOT"

%files -n %libname
%defattr(-,root,root)
%{_libdir}/libgeglmm.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%{_libdir}/pkgconfig/geglmm.pc
%{_includedir}/geglmm-1.0/*
%{_libdir}/geglmm-1.0/*
%{_libdir}/libgeglmm.so
%{_libdir}/libgeglmm.la

