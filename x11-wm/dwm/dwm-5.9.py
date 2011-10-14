metadata = """
summary @ A dynamic window manager for X11
homepage @ http://www.suckless.org/dwm/
license @ MIT
src_url @ http://dl.suckless.org/dwm/$fullname.tar.gz
arch @ ~x86
options @ xinerama
"""

depends = """
common @ x11-libs/libX11
"""

opt_build = """
xinerama @ x11-libs/libXinerama x11-proto/xineramaproto
"""

def prepare():
    copy("%s/config.h" % filesdir, "config.h")
    sed("-i 's/CPPFLAGS =/CPPFLAGS +=/g' config.mk")
    sed("-i 's/^CFLAGS = -g/#CFLAGS += -g/g' config.mk")
    sed("-i 's/^#CFLAGS = -std/CFLAGS += -std/g' config.mk")
    sed("-i 's/^LDFLAGS = -g/#LDFLAGS += -g/g' config.mk")
    sed("-i 's/^#LDFLAGS = -s/LDFLAGS += -s/g' config.mk")

def build():
    if opt("xinerama"):
        make('X11INC=/usr/include/X11 X11LIB=/usr/lib/X11 XINERAMAFLAGS="" XINERAMALIBS=""')
    else:
        make("X11INC=/usr/include/X11 X11LIB=/usr/lib/X11")

def install():
    raw_install("PREFIX=/usr DESTDIR=%s" % install_dir)
    insdoc("LICENSE", "README")
    insfile("%s/dwm.desktop" % filesdir, "/usr/share/xsessions/dwm.desktop")
