%global glib2_version 2.44
%global ostree_version 2017.14
%global flatpak_version 0.99.1

Name:           flatpak-builder
Version:        1.0.14
Release:        2%{?dist}
Summary:        Tool to build flatpaks from source

# src/builder-utils.c has portions derived from GPLv2+ code,
# the rest is LGPLv2+
License:        LGPLv2+ and GPLv2+
URL:            http://flatpak.org/
Source0:        https://github.com/flatpak/flatpak-builder/releases/download/%{version}/%{name}-%{version}.tar.xz

# https://github.com/flatpak/flatpak-builder/pull/464
# https://bugzilla.redhat.com/show_bug.cgi?id=2042007
Patch0:         flatpak-builder-CVE-2022-21682.patch

BuildRequires:  gettext
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  flatpak >= %{flatpak_version}
BuildRequires:  elfutils-devel
BuildRequires:  libcap-devel
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(ostree-1) >= %{ostree_version}
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  /usr/bin/xmlto
BuildRequires:  /usr/bin/xsltproc

Requires:       flatpak%{?_isa} >= %{flatpak_version}
Requires:       glib2%{?_isa} >= %{glib2_version}
Requires:       ostree-libs%{?_isa} >= %{ostree_version}
Requires:       /usr/bin/bzip2
%if ! 0%{?rhel} > 7
# No bzr in latest RHEL
Recommends:     /usr/bin/bzr
%endif
Requires:       /usr/bin/eu-strip
Requires:       /usr/bin/git
Requires:       /usr/bin/patch
Requires:       /usr/bin/rofiles-fuse
Requires:       /usr/bin/strip
Recommends:     /usr/bin/svn
Requires:       /usr/bin/tar
Requires:       /usr/bin/unzip

%description
Flatpak-builder is a tool for building flatpaks from sources.

See http://flatpak.org/ for more information.


%prep
%autosetup -p1


%build
%configure \
    --enable-docbook-docs

%make_build V=1


%install
%make_install


%files
%license COPYING
%doc %{_pkgdocdir}
%{_bindir}/flatpak-builder
%{_mandir}/man1/flatpak-builder.1*
%{_mandir}/man5/flatpak-manifest.5*


%changelog
* Fri Apr 01 2022 Debarshi Ray <rishi@fedoraproject.org> - 1.0.14-2
- Fix CVE-2022-21682 (#2042007)

* Wed Mar 09 2022 Debarshi Ray <rishi@fedoraproject.org> - 1.0.14-1
- Update to 1.0.14 (#2047312)

* Tue Feb 25 2020 David King <dking@redhat.com> - 1.0.9-3
- Use elfutils instead of libdwarf (#1613030)

* Fri Nov 08 2019 David King <dking@redhat.com> - 1.0.9-2
- Drop Requires on lzip (#1748290)

* Fri Nov 08 2019 David King <dking@redhat.com> - 1.0.9-1
- Rebase to 1.0.9 (#1748290)

* Tue Oct 16 2018 Kalev Lember <klember@redhat.com> - 1.0.1-2
- Change svn requires to recommends (#1639355)

* Thu Oct 04 2018 Kalev Lember <klember@redhat.com> - 1.0.1-1
- Update to 1.0.1

* Mon Aug 20 2018 David King <amigadave@amigadave.com> - 1.0.0-1
- Update to 1.0.0

* Mon Aug 13 2018 Kalev Lember <klember@redhat.com> - 0.99.3-2
- Update license to "LGPLv2+ and GPLv2+"

* Thu Aug 02 2018 David King <dking@redhat.com> - 0.99.3-1
- Import from Fedora
