#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	Simple, small, efficient, C++ XML parser
Summary(pl.UTF-8):	Prosty, mały, efektywny parser XML w C++
Name:		tinyxml2
Version:	4.0.1
Release:	1
License:	BSD-like
Group:		Libraries
#Source0Download: https://github.com/leethomason/tinyxml2/releases
Source0:	https://github.com/leethomason/tinyxml2/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	36aed868b751e728fa8f714aa3376a1d
URL:		https://github.com/leethomason/tinyxml2
BuildRequires:	cmake >= 2.6
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TinyXML-2 is a simple, small, efficient, C++ XML parser that can be
easily integrated into other programs.

%description -l pl.UTF-8
TinyXML-2 to prosty, mały, efektywny parser XML w C++, który można
łatwo integrować w innych programach.

%package devel
Summary:	Header files for TinyXML-2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki TinyXML-2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for TinyXML-2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki TinyXML-2.

%package static
Summary:	Static TinyXML-2 library
Summary(pl.UTF-8):	Statyczna biblioteka TinyXML-2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static TinyXML-2 library.

%description static -l pl.UTF-8
Statyczna biblioteka TinyXML-2.

%prep
%setup -q

%build
%cmake . \
	%{?with_static_libs:-DBUILD_STATIC_LIBS=ON}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc readme.md
%attr(755,root,root) %{_libdir}/libtinyxml2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtinyxml2.so.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtinyxml2.so
%{_includedir}/tinyxml2.h
%{_pkgconfigdir}/tinyxml2.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libtinyxml2.a
%endif
