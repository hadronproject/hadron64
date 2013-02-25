metadata = """
summary @ A library that read information about processes and the running system
homepage @ http://www.gnome.org/
license @ LGPL
src_url @ http://ftp.gnome.org/pub/gnome/sources/$name/2.28/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glib x11-libs/libXau sys-apps/texinfo
build @ dev-util/intltool dev-libs/gobject-introspection
"""

def configure():
    conf("-with-libgtop-smp")

def build():
    export("HOME", build_dir)
    make()

def install():
    export("HOME", build_dir)
    raw_install("DESTDIR=%s" % install_dir)
