pkgname = "scenefx"
pkgver = "0.1"
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
]
pkgdesc = "Drop-in replacement for the wlroots scene api for SwayFX"
maintainer = "bikoil <biko@atl.tools>"
license = "MIT"
url = "https://github.com/wlrfx/scenefx"
source = f"https://github.com/wlrfx/scenefx/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "f5c889f4c826a4216628bf1e7e48071fc33e7774b5e3d51e6fee6e571e420827"


