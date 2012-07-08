metadata = """
summary @ Make depend
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/util/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
build @ x11-proto/xproto
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)
