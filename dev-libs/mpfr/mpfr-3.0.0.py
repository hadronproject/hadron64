metadata = """
summary @ Multiple-precision floating-point library
homepage @ http://www.mpfr.org
license @ LGPL
src_url @ http://www.mpfr.org/$fullname/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ dev-libs/gmp
"""

def prepare():
    patch(level=1)

def configure():
    conf("--enable-thread-safe"
        "--enable-shared")

def install():
    raw_install('DESTDIR=%s install' % install_dir)
