metadata = """
summary @ A free library for arbitrary precision arithmetic
homepage @ http://gmplib.org
license @ LGPL-3
src_url @ ftp://ftp.gnu.org/gnu/$name/$fullname.tar.bz2
arch @ ~x86_64
"""

def configure():
    conf(
            "--enable-cxx",
            "--enable-mpbsd"
        )

def build():
    make()
    make("check")

def install():
    raw_install("DESTDIR=%s install" % install_dir)
