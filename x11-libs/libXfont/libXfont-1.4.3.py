metadata = """
summary @ X11 font rasterisation library
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/archive/individual/lib/libXfont-$version.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc media-libs/freetype x11-libs/libfontenc x11-proto/xproto 
          x11-proto/fontsproto x11-libs/xtrans
build @ x11-misc/util-macros x11-libs/xtrans
"""

def configure():
    conf("--disable-static")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    
    insdoc("COPYING")
