metadata = """
summary @ Library for the arithmetic of complex numbers with arbitrarily high precision.
homepage @ http://www.multiprecision.org/
license @ LGPL
src_url @ http://www.multiprecision.org/mpc/download/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
common @ >=dev-libs/mpfr-3.0.0 >=dev-libs/gmp-4.3.2
"""

def prepare():
    patch("libmpc_autoreconf_fix.patch")
    patch("libmpc-0.9-configure_cflags_egrep_issue.patch", level=1)
    aclocal()
    automake("--add-missing")
    autoreconf()

def install():
    raw_install("DESTDIR=%s install" % install_dir)
