metadata = """
summary @ Javascript Bindings for GNOME
homepage @ http://live.gnome.org/Gjs
license @ MIT MPL-1.1 LGPL-2 GPL-2
src_url @ http://download.gnome.org/sources/$name/1.30/$fullname.tar.xz
arch @ ~x86
"""

depends = """
common @ >=sys-libs/glib-2.30 >=dev-libs/gobject-introspection-1.29.16 
dev-libs/dbus-glib sys-apps/readline x11-libs/cairo 
>=dev-lang/spidermonkey-1.8.5
"""

install = lambda: raw_install("DESTDIR=%s" % install_dir)
build = lambda: (export("HOME", build_dir), make())

def configure():
    conf("--with-js-package=mozjs185",
            "--disable-systemtap",
            "--disable-dtrace",
            "--disable-coverage")
