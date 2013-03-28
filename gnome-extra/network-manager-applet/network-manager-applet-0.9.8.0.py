metadata = """
summary @ GNOME applet for NetworkManager
homepage @ http://projects.gnome.org/NetworkManager
license @ GPL-2
src_url @ ftp://ftp.gnome.org/pub/gnome/sources/$name/0.9/$fullname.tar.xz
arch @ ~x86_64
"""

depends = """
common @ >=sys-libs/glib-2.26 >=dev-libs/dbus-glib-0.88 >=gnome-base/libgnome-keyring-2.20 
>=sys-apps/dbus-1.4.1 >=sys-auth/polkit-0.96-r1 >=x11-libs/gtk+-3:3 >=x11-libs/libnotify-0.7.0 
app-i18n/iso-codes >=net-misc/networkmanager-0.9.6
"""

def configure():
    raw_configure("--prefix=/usr",
            "--sysconfdir=/etc",
            "--libexecdir=/usr/lib/NetworkManager"
            "--with-gtkver=3",
            "--disable-migration",
            "--disable-static")

def install():
    installd()
    insdoc("AUTHORS", "ChangeLog", "NEWS", "README")



