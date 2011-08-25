metadata = """
summary @ Desktop notification library
homepage @ http://library.gnome.org/devel/notification-spec/
license @ LGPL
src_url @ http://ftp.gnome.org/pub/GNOME/sources/$name/0.7/$fullname.tar.bz2
options @ test introspection
arch @ ~x86
"""

depends = """
runtime @ x11-libs/gdk-pixbuf
build @ x11-libs/gtk+
"""

def prepare():
    patch()

def configure():
    autoreconf()
    conf("--disable-static",
            config_enable("test", "tests"),
            config_enable("introspection"))

def build():
    export("HOME", build_dir)
    make()

def install():
    export("HOME", build_dir)
    raw_install("DESTDIR=%s" % install_dir)
