pkgname = "kaccounts-providers"
pkgver = "24.08.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "intltool",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kaccounts-integration-devel",
    "ki18n-devel",
    "kio-devel",
    "kpackage-devel",
    "libaccounts-qt-devel",
    "qcoro-devel",
    "signond-devel",
]
pkgdesc = "KDE providers for online accounts"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/network/kaccounts-providers"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kaccounts-providers-{pkgver}.tar.xz"
sha256 = "1528058dcc92f854e31f27fd6c86a82ea5df34bc3b7ab942d69ff0ac7f00d843"
hardening = ["vis"]


if self.profile().arch in ["aarch64", "ppc64le", "x86_64"]:
    makedepends += ["qt6-qtwebengine-devel"]
