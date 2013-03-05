metadata = """
summary @ X Rendering Extension client library
homepage @ http://xorg.freedesktop.org/
license @ MIT
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libXrender-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ x11-proto/renderproto x11-libs/libX11
"""


def configure():
    conf("--disable-static")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("COPYING")
