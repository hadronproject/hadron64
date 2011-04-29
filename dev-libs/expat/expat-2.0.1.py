metadata = """
summary @ An XML parser library
homepage @ http://expat.sourceforge.net
license @ MIT
src_url @ http://downloads.sourceforge.net/sourceforge/expat/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc
"""

def prepare():
    patch(level=1)

def install():
    raw_install("DESTDIR=%s install" % install_dir)
    insdoc("COPYING")
