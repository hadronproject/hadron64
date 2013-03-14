metadata = """
summary @ GNOME keyring client library
homepage @ http://www.gnome.org
license @ GPL LGPL
src_url @ http://ftp.gnome.org/pub/gnome/sources/$name/3.6/$fullname.tar.xz
arch @ ~x86_64
"""

depends = """
runtime @ sys-apps/dbus dev-libs/libgcrypt sys-libs/glib
build @ app-arch/xz
"""

def configure():
    conf("-disable-static",
            "--libexecdir=/usr/lib/gnome-keyring")

def install():
    raw_install("DESTDIR=%s" % install_dir)
