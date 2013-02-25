metadata = """
summary @ Window Navigator Construction Kit
homepage @ http://www.gnome.org/
license @ LGPL
src_url @ http://ftp.gnome.org/pub/gnome/sources/$name/2.30/$fullname.tar.bz2
arch @ ~x86_64
options @ introspection startup-notification
"""

depends = """
runtime @ x11-libs/gtk+:2  x11-libs/libXres x11-libs/libX11 sys-libs/glib
build @ dev-util/intltool x11-libs/libXt sys-devel/gettext dev-util/pkg-config
"""

opt_build = """
introspection @ dev-libs/gobject-introspection
startup-notification @ x11-libs/startup-notification
"""

def configure():
    conf("--disable-static",
        config_enable("startup-notification"),
        config_enable("introspection"))

def build():
    export("HOME", build_dir)
    make()

def install():
    export("HOME", build_dir)
    raw_install("DESTDIR=%s" % install_dir)
