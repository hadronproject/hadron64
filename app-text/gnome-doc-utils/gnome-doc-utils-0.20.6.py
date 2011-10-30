metadata = """
summary @ A collection of documentation utilities for the Gnome project
homepage @ http://live.gnome.org/GnomeDocUtils
license @ GPL2 LGPL2.1
src_url @ http://ftp.gnome.org/pub/gnome/sources/$name/0.20/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ app-text/rarian app-text/docbook-xml-dtd dev-libs/libxslt
build @ dev-util/pkg-config dev-util/intltool
"""

def configure():
    conf("--disable-scrollkeeper")

def build():
    export("PYTHONDONTWRITEBYTECODE", "1")
    make()

def install():
    raw_install("DESTDIR=%s" % install_dir)
