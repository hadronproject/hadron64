metadata = """
summary @ Display graphical dialog boxes from shell scripts
homepage @ http://www.gnome.org
license @ LGPL
src_url @ http://ftp.gnome.org/pub/gnome/sources/$name/3.2/$name-$version.tar.bz2
arch @ ~x86_64
options @ libnotify
"""

depends = """
runtime @ >=x11-libs/gtk+-3.0.0 >=sys-libs/glib-2.8
build @ app-text/docbook-xml-dtd:4.1.2 >=dev-util/intltool-0.40
>=sys-devel/gettext-0.14 >=dev-util/pkg-config-0.9 >=app-text/gnome-doc-utils-0.10.1
"""

opt_runtime = """
libnotify @ >=x11-libs/libnotify-0.6.1
"""

def configure():
    conf(
    "--disable-scrollkeeper",
    config_enable("libnotify"))

def build():
    export("PYTHONDONTWRITEBYTECODE", "1")
    make()

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("AUTHORS", "ChangeLog", "HACKING", "NEWS", "README", "THANKS", "TODO")
