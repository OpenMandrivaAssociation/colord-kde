Summary:	Colord support for KDE
Name:		colord-kde
Version:	0.5.0
Release:	3
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
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(xrandr)
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

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/colord-kde-icc-importer
%{_libdir}/qt5/plugins/*.so
%{_datadir}/applications/colordkdeiccimporter.desktop
%{_datadir}/kservices5/kcm_colord.desktop
%{_datadir}/kservices5/kded/colord.desktop
