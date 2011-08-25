metadata = """
summary @ Introspection system for GObject-based libraries
homepage @ http://live.gnome.org/GObjectInstrospection
license @ LGPL + GPL
src_url @ http://ftp.gnome.org/pub/gnome/sources/$name/0.10/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glib dev-libs/libffi dev-lang/python
"""

def configure():
    export("HOME", build_dir)
    autoreconf("-fi")
    conf("--disable-static")

def build():
    export("HOME", build_dir)
    make()

def install():
    raw_install("DESTDIR=%s" % install_dir)
