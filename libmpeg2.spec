Summary:	MPEG-2 Decoder
Name:		libmpeg2
Version:	0.5.1
Release:	7
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://libmpeg2.sourceforge.net/files/%{name}-%{version}.tar.gz
# Source0-md5:	0f92c7454e58379b4a5a378485bbd8ef
URL:		http://libmpeg2.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-libXv-devel
Obsoletes:	mpeg2dec
Obsoletes:	mpeg2dec-lib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-DCOFFEE_BREAK=1

%description
MPEG-2 Decoder.

%package devel
Summary:	MPEG-2 Decoder development files
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	SDL-devel
Requires:	xorg-libXext-devel
Requires:	xorg-libXv-devel
Obsoletes:	mpeg2dec-devel

%description devel
MPEG-2 Decoder development files.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static	\
	--enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/corrupt_mpeg2
%attr(755,root,root) %{_bindir}/extract_mpeg2
%attr(755,root,root) %{_bindir}/mpeg2dec
%attr(755,root,root) %ghost %{_libdir}/libmpeg2.so.?
%attr(755,root,root) %ghost %{_libdir}/libmpeg2convert.so.?
%attr(755,root,root) %{_libdir}/libmpeg2.so.*.*.*
%attr(755,root,root) %{_libdir}/libmpeg2convert.so.*.*.*
%{_mandir}/man1/mpeg2dec.1*
%{_mandir}/man1/extract_mpeg2.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmpeg2.so
%attr(755,root,root) %{_libdir}/libmpeg2convert.so
%{_includedir}/mpeg2dec
%{_pkgconfigdir}/libmpeg2.pc
%{_pkgconfigdir}/libmpeg2convert.pc

