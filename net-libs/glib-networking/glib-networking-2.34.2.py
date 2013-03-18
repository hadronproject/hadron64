metadata = """
summary @ Network-related giomodules for glib
homepage @ http://www.gtk.org/
license @ GPL-2
src_url @ ftp://ftp.gnome.org/pub/gnome/sources/$name/2.34/$fullname.tar.xz
arch @ ~x86_64
options @ ssl gnome
"""

depends = """
common @ >=sys-libs/glib-2.34
"""

opt_common = """
ssl @ app-misc/ca-certificates >=net-libs/gnutls-2.11.0
gnome @ gnome-base/gsettings-desktop-schemas
"""

def configure():
    conf("--libexecdir=/usr/lib/glib-networking",
            "--disable-static",
            "--with-ca-certificates=/etc/ssl/certs/ca-certificates.crt",
            config_with("gnome", "gnome-proxy"),
            config_with("ssl", "gnutls"))

install = lambda: installd()

