metadata = """
summary @ 11 miscellaneous extensions library
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libXext-$version.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc x11-libs/libX11 x11-proto/xextproto
"""

#srcdir = "libXext-%s" % version

def configure():
    conf("--disable-static")


def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
