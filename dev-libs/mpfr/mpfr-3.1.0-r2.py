metadata = """
summary @ Multiple-precision floating-point library
homepage @ http://www.mpfr.org
license @ LGPL
src_url @ http://www.mpfr.org/$fullname/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ dev-libs/gmp
"""

def prepare():
    patch("mpfr-3.1.0.p10.patch", level=1)

def configure():
    conf("--enable-thread-safe",
        "--enable-shared")

def install():
    raw_install('DESTDIR=%s install' % install_dir)
