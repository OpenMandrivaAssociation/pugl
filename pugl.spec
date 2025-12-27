%define commit b6f4c6b500d3c416b0406f1f9e0bf5c7d873a1b3
%define gitdate	20251215

%define	api 0
%define	major 0
%define	libname %mklibname %{name} %{api} %{major}
%define	devname %mklibname %{name} -d

Summary:	PlUgin Graphics Library
Name:	pugl
Version:	0.5.7
Release:	0.%{gitdate}.1
License:	ISC
Group:	System/Libraries
Url:		https://gitlab.com/lv2/pugl/
# No official releases: use a recent HEAD
#Source0:	https://github.com/lv2/pugl/archive/%%{commit}.tar.gz?/%%{name}-%%{commit}.tar.gz
Source0:	%{name}-%{gitdate}.tar.xz
BuildRequires:doxygen
BuildRequires:	glslang
BuildRequires:	meson
BuildRequires:	ninja
BuildRequires:	python-sphinx
BuildRequires:	python-sphinx_lv2_theme
BuildRequires:	python-sphinxygen
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(libglvnd)
BuildRequires:	pkgconfig(vulkan)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcb-sync)
BuildRequires:	pkgconfig(xcursor)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xrandr)

%description
Pugl (PlUgin Graphics Library) is a minimal portability layer for GUIs
which is suitable for use in plugins and applications. It works on X11,
MacOS, and Windows, and includes optional support for drawing with Vulkan,
OpenGL, and Cairo.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	PlUgin Graphics shared library
Group:		System/Libraries

%description -n %{libname}
PlUgin Graphics  shared library.

%files -n %{libname}
%doc AUTHORS README.md
%license COPYING LICENSES/*.txt
%{_libdir}/lib%{name}*-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	PlUgin Graphics development files
Group:		Development/Other
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
PlUgin Graphics development files.

%files -n %{devname}
%license COPYING LICENSES/*.txt
%{_docdir}/pugl-0
%{_includedir}/%{name}*-%{api}
%{_libdir}/lib%{name}*-%{api}.so
%{_libdir}/pkgconfig/%{name}*-%{api}.pc

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{gitdate}


%build
%meson
%meson_build


%install
%meson_install
