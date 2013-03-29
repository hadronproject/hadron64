metadata = """
summary @ Gtk module for bridging AT-SPI to Atk
homepage @ http://live.gnome.org/Accessibility
license @ LGPL-2
src_url @ ftp://ftp.gnome.org/pub/gnome/sources/at-spi2-atk/2.6/$fullname.tar.xz
arch @ ~x86_64
"""

depends = """
common @ >=app-accessibility/at-spi2-core-2.6 >=dev-libs/atk-2.1.0 sys-libs/glib >=sys-apps/dbus-1
"""

def configure():
    conf("--enable-p2p")

install = lambda: installd()

def post_install():
    if not system("glib-compile-schemas /usr/share/glib-2.0/schemas"):
        raise BuildError
