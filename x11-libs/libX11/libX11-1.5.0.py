metadata = """
summary @ X11 client-side library
homepage @ http://xorg.freedesktop.org/
license @ MIT
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libX11-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc x11-libs/libxcb x11-proto/xproto
          x11-proto/kbproto
build @ x11-misc/util-macros x11-proto/xextproto x11-libs/xtrans
        x11-proto/inputproto
"""

def configure():
    conf("--disable-static --disable-xf86bigfont")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("COPYING")
