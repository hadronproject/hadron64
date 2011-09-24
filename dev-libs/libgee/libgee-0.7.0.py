metadata = """
summary @ GObject-based interfaces and classes for commonly used data structures.
homepage @ http://live.gnome.org/Libgee
license @ LGPL-2.1
src_url @ http://ftp.gnome.org/pub/GNOME/sources/libgee/0.7/$fullname.tar.xz
options @ introspection static
arch @ ~x86
"""

depends = """
common @ >=sys-libs/glib-2.12
build @ dev-lang/vala
"""

opt_common = """
instrospection @ >=dev-libs/gobject-introspection-0.9.6
"""

def configure():
    conf(config_enable("static", "static-libs"), 
            config_enable("introspection"))

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("AUTHORS", "ChangeLog*", "MAINTAINERS", "NEWS", "README")
