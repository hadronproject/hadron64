metadata = """
summary @ GLib bindings for DBUS
homepage @ http://www.freedesktop.org/wiki/Software/DBusBindings
license @ GPL
src_url @ http://dbus.freedesktop.org/releases/$name/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glib sys-apps/dbus
"""

def configure():
    conf("--localstatedir=/var",
            "--enable-static=no", 
            "--enable-bash-completion=no")

def install():
    raw_install("DESTDIR=%s" % install_dir)

