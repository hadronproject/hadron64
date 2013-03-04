metadata = """
summary @ X.Org XTrap library
homepage @ http://xorg.freedesktop.org/
src_url @ http://xorg.freedesktop.org/releases/individual/lib/$fullname.tar.bz2
license @ MIT
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/libX11 x11-libs/libXt x11-libs/libXext
build @ x11-proto/trapproto
"""

def configure():
    conf("--disable-static")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("COPYING")
