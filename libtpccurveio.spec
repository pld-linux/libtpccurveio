Summary:	PET time-activity curve I/O library
Summary(pl.UTF-8):	Biblioteka PET time-activity curve I/O
Name:		libtpccurveio
Version:	1.4.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.turkupetcentre.net/software/libsrc/%{name}_%(echo %{version} | tr . _)_src.zip
# Source0-md5:	0b9f261af559c0e80db543931590225a
Patch0:		%{name}-shared.patch
URL:		http://www.turkupetcentre.net/software/libdoc/libtpccurveio/
BuildRequires:	libtpcmisc-devel >= 1.3.0
BuildRequires:	unzip
Requires:	libtpcmisc >= 1.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PET time-activity curve I/O library by Turku PET Centre.

%description -l pl.UTF-8
PET time-activity curve I/O - biblioteka wejścia/wyjścia krzywych
aktywności czasowej autorstwa Turku PET Centre.

%package devel
Summary:	Header files for libtpccurveio library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libtpccurveio
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libtpcmisc-devel >= 1.3.0

%description devel
Header files for libtpccurveio library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libtpccurveio.

%package static
Summary:	Static libtpccurveio library
Summary(pl.UTF-8):	Statyczna biblioteka libtpccurveio
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libtpccurveio library.

%description static -l pl.UTF-8
Statyczna biblioteka libtpccurveio.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make} libtpccurveio.la \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -std=gnu99 -Wall -I/usr/include/tpc -Iinclude \$(INCLUDE) \$(ANSI)" \
	LDFLAGS="%{rpmldflags}" \
	PET_LIB=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}

%{__make} libinstall \
	DESTDIR=$RPM_BUILD_ROOT \
	PET_LIB=%{_libdir}

install -d $RPM_BUILD_ROOT%{_includedir}/tpc
install include/*.h $RPM_BUILD_ROOT%{_includedir}/tpc

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc History Readme TODO
%attr(755,root,root) %{_libdir}/libtpccurveio.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtpccurveio.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtpccurveio.so
%{_libdir}/libtpccurveio.la
%{_includedir}/tpc/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libtpccurveio.a
