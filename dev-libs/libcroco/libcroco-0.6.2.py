metadata = """
summary @ GNOME CSS2 parsing and manipulation toolkit
homepage @ http://www.gnome.org/
license @ LGPL
src_url @ http://ftp.gnome.org/pub/gnome/sources/$name/0.6/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc sys-libs/glib dev-libs/libxml2
build @ dev-util/intltool dev-util/pkg-config
"""

def configure():
    conf("--disable-static")

def install():
    raw_install("DESTDIR=%s" % install_dir)
