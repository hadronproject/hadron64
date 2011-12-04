metadata = """
summary @ Python 2 bindings for GObject
homepage @ http://www.pygtk.org/
license @ LGPL
src_url @ http://ftp.gnome.org/pub/gnome/sources/$name/2.28/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glib dev-libs/gobject-introspection
build @ dev-lang/python dev-python/py2cairo
"""

def prepare():
    patch(level=1)
    autoreconf("-fi")

def configure():
    conf("--disable-introspection")

def install():
    linstall()
    #raw_install("DESTDIR=%s" % install_dir)
