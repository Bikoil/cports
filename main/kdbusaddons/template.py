pkgname = "kdbusaddons"
pkgver = "6.7.0"
pkgrel = 0
build_style = "cmake"
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
checkdepends = [
    "dbus",
]
pkgdesc = "KDE Widgets for configuration dialogs"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only OR LGPL-3.0-only"
url = "https://api.kde.org/frameworks/kdbusaddons/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kdbusaddons-{pkgver}.tar.xz"
sha256 = "e87d08f6d0037d8fa33f1e7d16a4e3aa17d7d0b12c6aa96f76323f78344e151b"
hardening = ["vis"]


@subpackage("kdbusaddons-devel")
def _(self):
    return self.default_devel()
