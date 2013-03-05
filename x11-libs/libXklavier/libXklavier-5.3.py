metadata = """
summary @ High level XKB library
homepage @ http://www.freedesktop.org/Software/LibXklavier
license @ LGPL-2
src_url @ http://ftp.acc.umu.se/pub/gnome/sources/libxklavier/5.1/libxklavier-5.1.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glib x11-libs/libxkbfile dev-libs/libxml2 x11-libs/libXi
          app-i18n/iso-codes
build @ dev-util/pkg-config
"""

srcdir = "libxklavier-%s" % version

def configure():
    conf("--with-xkb-base=/usr/share/X11/xkb --disable-static")

def install():
    raw_install("DESTDIR=%s" % install_dir)
