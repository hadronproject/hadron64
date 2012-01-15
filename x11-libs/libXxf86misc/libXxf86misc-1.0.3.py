metadata = """
summary @ X.Org Xxf86misc library
homepage @ http://xorg.freedesktop.org/
license @ MIT
src_url @ http://xorg.freedesktop.org/releases/individual/lib/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ x11-libs/libX11 x11-libs/libXext x11-proto/xproto x11-proto/xextproto x11-proto/xf86miscproto
"""

def configure():
    conf("--disable-static")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insfile("COPYING", "/usr/share/licenses/%s" % name)
