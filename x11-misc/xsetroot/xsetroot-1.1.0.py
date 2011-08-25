metadata = """
summary @  Classic X utility to set your root window background to a given pattern or color
homepage @  http://xorg.freedesktop.org/
license @  custom
src_url @  http://xorg.freedesktop.org/archive/individual/app/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ x11-libs/libXcursor x11-libs/libX11 x11-libs/libXmu
build @ x11-misc/util-macros x11-misc/xbitmaps
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("COPYING")
