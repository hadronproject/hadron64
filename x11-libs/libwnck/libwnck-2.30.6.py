metadata = """
summary @ Window Navigator Construction Kit
homepage @ http://www.gnome.org/
license @ LGPL
src_url @ http://ftp.gnome.org/pub/gnome/sources/$name/2.30/$fullname.tar.bz2
arch @ ~x86
"""


depends = """
runtime @ x11-libs/gtk+ x11-libs/startup-notification x11-libs/libXres
build @ dev-util/intltool x11-libs/libXt
"""

def configure():
    conf("--disable-static",
        "--disable-introspection")

def install():
    raw_install("DESTDIR=%s" % install_dir)
