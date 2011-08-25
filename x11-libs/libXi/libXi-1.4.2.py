metadata = """
summary @ X11 Input extension library
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libXi-$version.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc x11-libs/libXext x11-proto/inputproto
build @ x11-misc/util-macros
"""

#srcdir = "libXi-%s" % version

def configure():
    conf("--disable-static")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
