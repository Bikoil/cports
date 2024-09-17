pkgname = "zlib-ng-compat"
pkgver = "2.2.2"
# compat version
_cver = "1.3.1"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--prefix=/usr",
    "--shared",
    "--zlib-compat",
]
hostmakedepends = ["pkgconf"]
# we need to explicitly provide higher ver or apk won't upgrade it,
# even with provider_priority set which is strange but it is how it is
provides = [
    f"so:libz.so.1={_cver}.99",
    f"zlib={_cver}-r99",
]
replaces = [f"zlib<{_cver}-r99"]
pkgdesc = "Implementation of zlib compression library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Zlib"
url = "https://github.com/zlib-ng/zlib-ng"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "fcb41dd59a3f17002aeb1bb21f04696c9b721404890bb945c5ab39d2cb69654c"
tool_flags = {"CFLAGS": ["-fPIC"]}
compression = "deflate"
# sigh, carried over from zlib's old buildsystem
options = ["bootstrap", "linkundefver"]


@subpackage("zlib-ng-compat-devel-static")
def _(self):
    self.provides = [f"zlib-devel-static={_cver}-r99"]
    self.replaces = [f"zlib-devel-static<{_cver}-r99"]

    return ["usr/lib/*.a"]


@subpackage("zlib-ng-compat-devel")
def _(self):
    self.provides = [f"zlib-devel={_cver}-r99"]
    self.replaces = [f"zlib-devel<{_cver}-r99"]

    return self.default_devel()


@subpackage("zlib-dbg")
def _(self):
    self.subdesc = "transitional debug package"
    # prevent cbuild from thinking it's a depcycle
    self.depends = [f"virtual:zlib-ng-compat-dbg={self.full_pkgver}!base-files"]
    self.options = ["empty"]
    return []
