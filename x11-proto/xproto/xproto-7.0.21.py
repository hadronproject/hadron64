metadata = """
summary @ X11 core wire protocol and auxiliary headers
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/proto/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ x11-misc/util-macros
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
