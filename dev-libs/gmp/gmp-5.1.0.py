metadata = """
summary @ A free library for arbitrary precision arithmetic
homepage @ http://gmplib.org
license @ LGPL-3
src_url @ ftp://ftp.gmplib.org/pub/gmp-$version/gmp-$version.tar.xz
options @ cxx
arch @ ~x86_64
"""

def configure():
    conf(config_enable("cxx"))

def install():
    raw_install("DESTDIR=%s install" % install_dir)
