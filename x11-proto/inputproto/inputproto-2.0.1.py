metadata = """
summary @ X11 Input extension wire protocol
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/proto/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
build @ x11-misc/util-macros
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)
    
    insdoc("COPYING")
