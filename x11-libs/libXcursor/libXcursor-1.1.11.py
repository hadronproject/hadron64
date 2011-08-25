metadata = """
summary @ X cursor management library
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libXcursor-$version.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ x11-libs/libXfixes x11-libs/libXrender
"""

#srcdir = "libXcursor-%s" % version

def configure():
    conf("--disable-static")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
