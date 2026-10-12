%global elf_version 0.8.12
%global glib2_version 2.44
%global libdw_version 0.172
%global ostree_version 2017.14
%global flatpak_version 0.99.1

Name:           flatpak-builder
Version:        1.2.3
Release:        2%{?dist}
Summary:        Tool to build flatpaks from source

# src/builder-utils.c has portions derived from GPLv2+ code,
# the rest is LGPLv2+
License:        LGPLv2+ and GPLv2+
URL:            http://flatpak.org/
Source0:        https://github.com/flatpak/flatpak-builder/releases/download/%{version}/%{name}-%{version}.tar.xz

# CVE-2026-86320
# https://github.com/flatpak/flatpak-builder/commit/6a01485332969e8d46f100ec1f8d6ea458cfd468
Patch0:         builder-source-patch-disable-git-hooks-completely-when-applying-patches.patch

BuildRequires:  gettext
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  flatpak >= %{flatpak_version}
BuildRequires:  libcap-devel
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libdw) >= %{libdw_version}
BuildRequires:  pkgconfig(libelf) >= %{elf_version}
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(ostree-1) >= %{ostree_version}
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  /usr/bin/xmlto
BuildRequires:  /usr/bin/xsltproc

Requires:       elfutils-libelf%{?_isa} >= %{elf_version}
Requires:       elfutils-libs%{?_isa} >= %{libdw_version}
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
Recommends:     /usr/bin/zstd

%description
Flatpak-builder is a tool for building flatpaks from sources.

See http://flatpak.org/ for more information.


%prep
%autosetup -p1


%build
%configure \
    --enable-docbook-docs \
    --with-fuse=2

%make_build V=1


%install
%make_install


%files
%license COPYING
%doc %{_pkgdocdir}
%{_bindir}/flatpak-builder
%{_libexecdir}/flatpak-builder-debugedit
%{_mandir}/man1/flatpak-builder.1*
%{_mandir}/man5/flatpak-manifest.5*


%changelog
* Fri Oct 02 2026 Luigi Pavan <lpavan@redhat.com> - 1.2.3-2
- Disable git hooks when applying patches (CVE-2026-86320)
  Resolves: RHEL-262183

* Wed Nov 08 2023 Debarshi Ray <rishi@fedoraproject.org> - 1.2.3-1
- Rebase to 1.2.3 (RHEL-16011)

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
