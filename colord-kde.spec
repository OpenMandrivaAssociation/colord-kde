Summary:	Colord support for KDE
Name:		colord-kde
Version:	0.5.0
Release:	1
License:	GPLv2+
Group:		Graphics
Url:		http://dantti.wordpress.com/
Source0:	http://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	pkgconfig(xcb-randr)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xkb)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5ItemViews)
Requires:	colord

%description
KDE support for colord including KDE Daemon module and System Settings module.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files
%{_kde_applicationsdir}/colordkdeiccimporter.desktop
%{_kde_bindir}/colord-kde-icc-importer
%{_kde_libdir}/kde4/k*_colord.so
%{_kde_services}/kcm_colord.desktop
%{_kde_services}/kded/colord.desktop
