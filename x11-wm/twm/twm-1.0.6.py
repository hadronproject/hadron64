metadata = """
summary @ Tab Window Manager for the X Window System
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/app/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/libX11 x11-libs/libXext x11-libs/libXt x11-libs/libXmu x11-libs/libICE  x11-libs/libSM
build @ sys-devel/bison
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
