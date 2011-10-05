metadata = """
summary @ Fast, easy, and free BitTorrent client
homepage @ http://www.transmissionbt.com/
license @ MIT
src_url @ http://mirrors.m0k.org/transmission/files/$name-$version.tar.bz2
arch @ ~x86
options @ gtk libnotify libcanberra utp qt nls
"""

depends = """
runtime @ dev-libs/dbus-glib dev-libs/libevent net-misc/curl dev-util/intltool
build @ sys-devel/gettext dev-util/intltool dev-util/pkg-config sys-apps/sed
"""

opt_runtime = """
gtk @ x11-libs/gtk+:2 dev-libs/dbus-glib
    libnotify @ x11-libs/libnotify
    libcanberra @ media-libs/libcanberra
qt @ x11-libs/qt
nls @ sys-devel/gettext dev-util/intltool
"""

def configure():
    conf(
    " --disable-gconf2",
    config_enable("gtk"),
    config_enable("utp"),
    config_enable("libcanberra"),
    config_enable("libnotify"),
    config_enable("nls"))

def build():
    make()
    if opt("qt"):
        cd("qt")
        system("qmake qtr.pro")

def install():
    for nav in ("daemon", "cli", "web", "utils", "gtk", "po"):
        raw_install("-C %s DESTDIR=%s" % (nav, install_dir))

    if opt("qt"):
        raw_install("-C qt INSTALL_ROOT=%s" % install_dir)

    insdoc("COPYING")

    insfile("qt/transmission-qt.desktop", "/usr/share/applications/transmission-qt.desktop")
    insfile("qt/icons/transmission.png", "/usr/share/pixmaps/transmission-qt.png")
    insfile("%s/transmissiond.conf" % filesdir, "/etc/conf.d/transmissiond")
    insexe("%s/transmissiond" % filesdir, "/etc/rc.d/transmissiond")

def post_install():

#cli icin
    notify("If you want to run the Transmission daemon at boot, add transmissiond to the DAEMONS array in /etc/rc.conf. You have to set the user in /etc/conf.d/transmissiond.")

    if opt("gtk"):
        system("gtk-update-icon-cache -q -t -f /usr/share/icons/hicolor")

    if opt("gtk") or opt("qt"):
        system("update-desktop-database -q")
