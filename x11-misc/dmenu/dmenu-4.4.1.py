metadata = """
summary @ A generic menu for X
homepage @ http://tools.suckless.org/dmenu
license @ MIT
src_url @ http://dl.suckless.org/tools/$fullname.tar.gz
arch @ ~x86
"""

depends = """
common @ x11-libs/libXinerama
"""

def build():
    make("X11INC=/usr/include/X11 X11LIB=/usr/lib/X11")

def install():
    raw_install("PREFIX=/usr DESTDIR=%s" % install_dir)
    insdoc("LICENSE")

