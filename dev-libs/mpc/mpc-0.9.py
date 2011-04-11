metadata = """
summary @ Library for the arithmetic of complex numbers with arbitrarily high precision.
homepage @ http://www.multiprecision.org/
license @ LGPL
src_url @ http://www.multiprecision.org/mpc/download/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ >=dev-libs/mpfr-3.0.0
"""

def prepare():
    patch(level=1)
    autoreconf()

def install():
    raw_install("DESTDIR=%s install" % install_dir)
