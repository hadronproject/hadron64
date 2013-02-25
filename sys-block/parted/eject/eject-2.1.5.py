metadata = """
summary @ A program for ejecting removable media under software control
homepage @ http://eject.sourceforge.net/
license @ GPL
src_url @ ftp://ftp.archlinux.org/other/eject/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
"""
srcdir = "eject"

def prepare():
    patch(level=0)


def install():
    raw_install("DESTDIR=%s" % install_dir)
