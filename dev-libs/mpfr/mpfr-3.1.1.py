metadata = """
summary @ Multiple-precision floating-point library
homepage @ http://www.mpfr.org
license @ LGPL
src_url @ http://www.mpfr.org/mpfr-current/mpfr-$version.tar.xz
arch @ ~x86_64
"""

depends = """
runtime @ >=dev-libs/gmp-5.0
"""

def prepare():
    patchlevel = "p2"
    patch("mpfr-3.1.1-%s" % patchlevel, level=1)

def configure():
    conf("--enable-thread-safe",
        "--enable-shared")

def install():
    raw_install('DESTDIR=%s install' % install_dir)
