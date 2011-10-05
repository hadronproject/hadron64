metadata = """
summary @ Allows you to load glade interface files in a program at runtime
homepage @ http://www.gnome.org/
license @ LGPL
src_url @ http://ftp.gnome.org/pub/gnome/sources/$name/2.6/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ x11-libs/gtk+:2 dev-libs/libxml2
build @ dev-lang/python dev-util/pkg-config
"""

def prepare():
    patch(level=1)

def configure():
    conf("--disable-static",
    "--disable-gtk-doc")

def install():
    #raw_install("DESTDIR=%s" % install_dir)
    linstall()
    insfile("libglade-convert", "/usr/bin/")
