pkgname = "kgamma"
pkgver = "6.2.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcmutils-devel",
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE tool for adjusting monitor gamma"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/plasma/kgamma"
source = f"$(KDE_SITE)/plasma/{pkgver}/kgamma-{pkgver}.tar.xz"
sha256 = "5244384ae28d92b0555e9c67d5995646ff9b10371eb36b07dd14b934779e6cfc"
hardening = ["vis"]
