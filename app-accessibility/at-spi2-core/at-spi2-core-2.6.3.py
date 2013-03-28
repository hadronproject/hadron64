metadata = """
summary @ D-Bus accessibility specifications and registration daemon
homepage @ http://live.gnome.org/Accessibility
license @ LGPL-2
src_url @ ftp://ftp.gnome.org/pub/gnome/sources/at-spi2-core/2.6/$fullname.tar.xz
arch @ ~x86_64
options @ introspection
"""

depends = """
common @ >=sys-libs/glib-2.28 >=sys-apps/dbus-1 x11-libs/libX11 x11-libs/libXi x11-libs/libXtst
"""

opt_common = """
introspection @ >=dev-libs/gobject-introspection-0.9.6
"""

def configure():
    conf("--prefix=/usr",
            "--sysconfdir=/etc",
            "--libexecdir=/usr/lib/at-spi2-core",
            config_enable("introspection"))

install = lambda: installd()
