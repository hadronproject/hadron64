metadata = """
summary @ A dynamic window manager for X11
homepage @ http://www.suckless.org/dwm/
license @ MIT
src_url @ http://dl.suckless.org/dwm/$fullname.tar.gz
arch @ ~x86_64
options @ xinerama
"""

depends = """
common @ x11-libs/libX11
"""

opt_build = """
xinerama @ x11-libs/libXinerama x11-proto/xineramaproto
"""

def prepare():
    copy("%s/config.h.6.0" % filesdir, "config.h")
    sed("""-i -e "s/CFLAGS = -std=c99 -pedantic -Wall -Os/CFLAGS += -std=c99 -pedantic -Wall -g/" \
        -e "/^LDFLAGS/{s|=|+=|g;s|-s ||g}" \
        -e "s/#XINERAMALIBS =/XINERAMALIBS ?=/" \
        -e "s/#XINERAMAFLAGS =/XINERAMAFLAGS ?=/" \
        -e "s@/usr/X11R6/include@/usr/include/X11@" \
        -e "s@/usr/X11R6/lib@/usr/lib@" \
        config.mk""")













    """sed("-i 's/CPPFLAGS =/CPPFLAGS +=/g' config.mk")
    sed("-i 's/^CFLAGS = -g/#CFLAGS += -g/g' config.mk")
    sed("-i 's/^#CFLAGS = -std/CFLAGS += -std/g' config.mk")
    sed("-i 's/^LDFLAGS = -g/#LDFLAGS += -g/g' config.mk")
    sed("-i 's/^#LDFLAGS = -s/LDFLAGS += -s/g' config.mk")"""
def build():
    if opt("xinerama"):
        make('X11INC=/usr/include/X11 X11LIB=/usr/lib/X11 XINERAMAFLAGS="" XINERAMALIBS=""')
    else:
        make("X11INC=/usr/include/X11 X11LIB=/usr/lib/X11", j=1)

def install():
    raw_install("PREFIX=/usr DESTDIR=%s" % install_dir)
    insdoc("LICENSE", "README")
    insfile("%s/dwm.desktop" % filesdir, "/usr/share/xsessions/dwm.desktop")
