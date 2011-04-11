metadata = """
summary @ A free library for arbitrary precision arithmetic
homepage @ http://gmplib.org
license @ LGPL-3
src_url @ ftp://ftp.gnu.org/gnu/$name/$fullname.tar.bz2
arch @ ~x86
"""

def configure():
    if arch == "x86":
        export("ABI", "32")
    conf("--enable-cxx")

def build():
    make()
    make("check")

def install():
    raw_install("DESTDIR=%s install" % install_dir)

