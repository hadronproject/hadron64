metadata = """
summary @ X11 Fixes extension wire protocol
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/proto/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc x11-proto/xproto x11-proto/xextproto
build @ x11-misc/util-macros
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
