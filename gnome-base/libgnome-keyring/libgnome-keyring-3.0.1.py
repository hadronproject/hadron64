metadata = """
summary @ GNOME keyring client library
homepage @ http://www.gnome.org
license @ GPL LGPL
src_url @ http://ftp.gnome.org/pub/gnome/sources/$name/3.0/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-apps/dbus dev-libs/libgcrypt sys-libs/glib
"""

def configure():
    conf("-disable-static",
            "--libexecdir=/usr/lib/gnome-keyring")

def install():
    raw_install("DESTDIR=%s" % install_dir)
