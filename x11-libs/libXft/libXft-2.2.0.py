metadata = """
summary @ FreeType-based font drawing library for X
homepage @ http://xorg.freedesktop.org/
license @ MIT
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libXft-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc media-libs/fontconfig x11-libs/libXrender
"""

def configure():
    conf("--disable-static")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
