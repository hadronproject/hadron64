metadata = """
summary @ C++ interface for glib2
homepage @ http://www.gtkmm.org
license @ LGPL-2.1 GPL-2
src_url @ http://ftp.gnome.org/pub/GNOME/sources/$name/2.28/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glib dev-libs/libsigc++ dev-util/pkg-config
"""

def configure():
    conf("--disable-schemas-compile",
            "--enable-deprecated-api")

def install():
    raw_install("DESTDIR=%s" % install_dir)
