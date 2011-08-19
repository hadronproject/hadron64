metadata = """
summary @ Library for applications dealing with netlink sockets
homepage @ http://www.infradead.org/~tgr/libnl/
license @ GPL
src_url @ http://www.infradead.org/~tgr/libnl/files/$name-$version.tar.gz
arch @ ~x86
slot @ 1.1
"""

depends = """
runtime @ sys-libs/glibc
"""

def prepare():
    patch(level=1)
