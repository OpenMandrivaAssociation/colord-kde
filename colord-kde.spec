Summary:	Colord support for KDE
Name:		colord-kde
Version:	0.3.0
Release:	2
License:	GPLv2+
Group:		Graphics
Url:		http://dantti.wordpress.com/
Source0:	http://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(colord)
BuildRequires:	pkgconfig(lcms2)
Requires:	kdebase4-runtime
Requires:	colord

%description
KDE support for colord including KDE Daemon module and System Settings module.

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%files
%doc COPYING MAINTAINERS TODO
%{_kde_applicationsdir}/colordkdeiccimporter.desktop
%{_kde_bindir}/colord-kde-icc-importer
%{_kde_libdir}/kde4/k*_colord.so
%{_kde_services}/kcm_colord.desktop
%{_kde_services}/kded/colord.desktop

