metadata = """
summary @ Library for writing single instance applications
homepage @ http://live.gnome.org/LibUnique
license @ LGPL
src_url @ http://ftp.gnome.org/pub/gnome/sources/$name/1.1/$fullname.tar.bz2
arch @ ~x86_64
options @ introspection
slot @ 1
"""

depends = """
common @ >=sys-libs/glib-2.25.7 x11-libs/libX11
build @ >=dev-util/pkg-config-0.17 
"""

opt_build = """
introspection @ x11-libs/gtk+:2[introspection] || x11-libs/gtk+:2
"""

def prepare():
    patch(level='1')

def configure():
    conf(
    "--disable-static",
    "--disable-maintainer-flags",
    "--disable-dbus",
    config_enable("introspection"))

def build():
    export("HOME", build_dir)
    make()

def install():
    installd()
