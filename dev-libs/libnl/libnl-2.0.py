metadata = """
summary @ Library for applications dealing with netlink sockets
homepage @ http://www.infradead.org/~tgr/libnl/
license @ GPL
src_url @ http://www.infradead.org/~tgr/libnl/files/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)

