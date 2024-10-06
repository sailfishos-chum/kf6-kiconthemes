%global  kf_version 6.6.0

Name:    kf6-kiconthemes
Version: 6.6.0
Release: 1%{?dist}
Summary: KDE Frameworks 6 Tier 3 integration module with icon themes
License: CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/kiconthemes
Source0:    %{name}-%{version}.tar.bz2

BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  kf6-extra-cmake-modules >= %{kf_version}
BuildRequires:  kf6-rpm-macros

BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  kf6-karchive-devel
BuildRequires:  kf6-breeze-icons-devel
BuildRequires:  kf6-kcolorscheme-devel
BuildRequires:  kf6-kconfigwidgets-devel
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kitemviews-devel
BuildRequires:  kf6-kwidgetsaddons-devel

BuildRequires:  pkgconfig(xkbcommon)

Requires:       breeze-icon-theme

%description
KDE Frameworks 6 Tier 3 integration module with icon themes

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_bindir}/kiconfinder6
%{_kf6_libdir}/libKF6IconThemes.so.*
%{_kf6_libdir}/libKF6IconWidgets.so.*
%{_kf6_qtplugindir}/kiconthemes6/iconengines/KIconEnginePlugin.so
%{_kf6_libdir}/qt6/qml/org/kde/iconthemes/
%{_kf6_datadir}/qlogging-categories6/kiconthemes.*

%files devel
%{_kf6_includedir}/KIconThemes
%{_kf6_includedir}/KIconWidgets
%{_kf6_libdir}/libKF6IconThemes.so
%{_kf6_libdir}/libKF6IconWidgets.so
%{_kf6_libdir}/cmake/KF6IconThemes/
%{_kf6_qtplugindir}/designer/kiconthemes6widgets.so
%{_qt6_docdir}/*.tags

%files doc
%{_qt6_docdir}/*.qch
