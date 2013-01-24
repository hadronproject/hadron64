metadata = """
summary @ Compression library implementing the deflate compression method found in gzip and PKZIP
homepage @ http://www.zlib.net
license @ ZLIB
src_url @ http://zlib.net/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
"""

def configure():
    raw_configure("--libdir=/usr/lib",
                "--includedir=/usr/include",
                "--prefix=/usr")

def install():
    raw_install('DESTDIR=%s LDCONFIG=: install' % install_dir)
    insdoc("FAQ", "README", "ChangeLog", "doc/algorithm.txt")
