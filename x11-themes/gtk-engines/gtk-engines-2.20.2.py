metadata = """
summary @ Theme engines for GTK+ 2
homepage @ http://live.gnome.org/GnomeArt
license @ GPL LGPL
src_url @ http://ftp.gnome.org/pub/gnome/sources/$name/2.20/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
build @ dev-util/pkg-config dev-util/intltool
"""

def configure():
    conf("--enable-animation")

def install():
    raw_install("DESTDIR=%s" % install_dir)
