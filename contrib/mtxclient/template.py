pkgname = "mtxclient"
pkgver = "0.10.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_LIB_EXAMPLES=OFF"]
make_check_args = [
    "-E",
    # need net
    "(BasicConnectivity|ClientAPI|MediaAPI|Encryption|Devices|Pushrules)",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "boost-devel",
    "gtest-devel",
    "olm-devel",
    "nlohmann-json",
    "coeurl-devel",
    "libevent-devel",
    "libcurl-devel",
    "re2-devel",
    "openssl-devel",
]
pkgdesc = "Client API library for the Matrix protocol"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/nheko-reborn/mtxclient"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9502e0a999d2873172d50bb80371c061266126c7d4db8e44447eb70c977b0230"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("mtxclient-devel")
def _devel(self):
    return self.default_devel()
