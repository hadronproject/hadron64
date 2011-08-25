metadata = """
summary @ notification daemon for the xfce desktop
homepage @ http://goodies.xfce.org/projects/applications/xfce4-notifyd
license @ GPL2
src_url @ http://archive.xfce.org/src/apps/$name/0.2/$fullname.tar.bz2
arch @ ~x86
options @ debug
"""

depends = """
runtime @ xfce-base/libxfce4ui x11-themes/hicolor-icon-theme x11-libs/gtk+ sys-apps/dbus dev-libs/dbus-glib
build @ dev-util/intltool dev-util/pkg-config sys-devel/gettext
"""

def configure():
    conf(
    "--prefix=/usr",
    "--sysconfdir=/etc",
    "--libexecdir=/usr/lib",
    "--localstatedir=/var",
    "--disable-static",
    config_enable("debug"))

def install():
    raw_install("DESTDIR=%s" % install_dir)


def post_install():
    system("gtk-update-icon-cache -q -t -f /usr/share/icons/hicolor")
