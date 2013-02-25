metadata = """
summary @ GLib bindings for DBUS
homepage @ http://www.freedesktop.org/wiki/Software/DBusBindings
license @ GPL
src_url @ http://dbus.freedesktop.org/releases/$name/$fullname.tar.gz
arch @ ~x86_64
options @ debug static-libs
"""

depends = """
runtime @ sys-libs/glib sys-apps/dbus
"""

def configure():
    conf("--localstatedir=/var",
            config_enable("static-libs", "static"),
            "--enable-bash-completion",
            config_enable("debug", "verbose-mode"),
            config_enable("debug", "asserts"))

def install():
    raw_install("DESTDIR=%s" % install_dir)
