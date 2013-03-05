metadata = """
summary @ 11 miscellaneous extensions library
homepage @ http://xorg.freedesktop.org/
license @ MIT
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libXext-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc x11-libs/libX11 x11-proto/xextproto
"""

def configure():
    conf("--disable-static")


def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("COPYING")
