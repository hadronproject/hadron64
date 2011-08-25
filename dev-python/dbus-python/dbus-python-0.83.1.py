metadata = """
summary @ Python bindings for DBUS
homepage @ http://www.freedesktop.org/wiki/Software/DBusBindings
license @ GPL + LGPL
src_url @ http://dbus.freedesktop.org/releases/$name/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ dev-libs/dbus-glib dev-lang/python
build @ dev-util/pkg-config
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)
