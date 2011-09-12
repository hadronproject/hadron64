metadata = """
summary @ A set of symbols and convience functions that all indicators would like to use
homepage @ http://launchpad.net/libindicator/
license @ GPL-3
src_url @ http://launchpad.net/$name/0.3/$version/+download/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ >=x11-libs/gtk+-2.18 >=sys-libs/glib-2.22
>=dev-libs/dbus-glib-0.76
"""

def configure():
    conf("--disable-static --with-gtk=2")

def install():
    raw_install("DESTDIR=%s -j1" % install_dir)
    insdoc("AUTHORS", "ChangeLog")

