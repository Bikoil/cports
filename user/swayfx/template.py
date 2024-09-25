pkgname = "swayfx"
pkgver = "0.4"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "libcap-progs",
    "meson",
    "pkgconf",
    "scdoc",
]
makedepends = [
    "cairo-devel",
    "gdk-pixbuf-devel",
    "json-c-devel",
    "pango-devel",
    "pcre2-devel",
    "wayland-devel",
    "wayland-protocols",
    "wlroots0.17-devel",
    "sway",
]
pkgdesc = "Sway, but with eyecandy!"
maintainer = "bikoil <biko@atl.tools>"
license = "MIT"
url = "https://github.com/WillPower3309/swayfx"
source = f"https://github.com/WillPower3309/swayfx/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "fa164734a7b32fd82f31e54c407b147e92247ef275de9df4a87b6198a36f20e2"
file_modes = {
    "usr/bin/sway": ("root", "root", 0o755),
}
file_xattrs = {
    "usr/bin/sway": {
        "security.capability": "cap_sys_nice+ep",
    },
}
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_file(
        self.files_path / "sway-portals.conf", "usr/share/xdg-desktop-portal"
    )


@subpackage("sway-backgrounds")
def _(self):
    self.subdesc = "backgrounds"
    self.install_if = [self.parent]

    return ["usr/share/backgrounds"]
