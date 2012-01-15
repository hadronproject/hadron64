metadata = """
summary @ X11 keyboard file manipulation library
homepage @ http://xorg.freedesktop.org/
license @ MIT
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libxkbfile-$version.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ x11-libs/libX11
build @ x11-misc/util-macros
"""

def configure():
    conf("--disable-static")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
