metadata = """
summary @ A lightweight C library which eases the writing of UNIX daemons
homepage @ http://0pointer.de/lennart/projects/libdaemon/
license @ LGPL
src_url @ http://0pointer.de/lennart/projects/libdaemon/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc
"""

def configure():
    conf("--disable-lynx")

def install():
    raw_install("DESTDIR=%s" % install_dir)
