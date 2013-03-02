metadata = """
summary @ Low-level cryptographic library
homepage @ http://www.lysator.liu.se/~nisse/nettle/
license @ LGPL-3 + LGPL-2.1
src_url @ http://www.lysator.liu.se/~nisse/archive/$fullname.tar.gz
arch @ ~x86_64
options @ gmp static-libs
"""

opt_build = """
gmp @ dev-libs/gmp
"""

def prepare():
    patch(level=1)
    autoreconf()

def configure():
    conf("--disable-openssl",
        config_enable("gmp", "public-key"),
        config_enable("static-libs", "static"))

def install():
    raw_install("DESTDIR=%s" % install_dir)
