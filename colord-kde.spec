Name:		colord-kde
Summary:	Colord support for KDE
Version:	0.2.0
Release:	1
License:	GPLv2+
Group:		Graphics
Source0:	http://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.bz2
BuildRequires:	cmake kdelibs4-devel colord-devel
BuildRequires:	lcms2-devel
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
%{_kde_libdir}/kde4/k*_colord.so
%{_kde_services}/kcm_colord.desktop
%{_kde_services}/kded/colord.desktop
%doc COPYING MAINTAINERS TODO
