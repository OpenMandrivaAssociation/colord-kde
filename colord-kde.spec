#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
Summary:	Colord support for KDE
Name:		colord-kde
Version:	25.12.0
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphics
Url:		https://dantti.wordpress.com/
%if 0%{?git:1}
Source0:	https://invent.kde.org/graphics/colord-kde/-/archive/%{gitbranch}/colord-kde-%{gitbranchd}.tar.bz2#/colord-kde-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%(if [ $(echo %{version} |cut -d. -f3) -ge 50 ]; then echo -n un; fi)stable/release-service/%{version}/src/colord-kde-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6DBus)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(xcb-randr)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(PlasmaQuick)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6ItemViews)
Requires:	colord

%rename plasma6-colord-kde

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
KDE support for colord including KDE Daemon module and System Settings module.

%files -f %{name}.lang
%{_bindir}/colord-kde-icc-importer
%{_libdir}/qt6/plugins/kf6/kded/colord.so
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_colord.so
%{_datadir}/applications/colordkdeiccimporter.desktop
%{_datadir}/applications/kcm_colord.desktop
