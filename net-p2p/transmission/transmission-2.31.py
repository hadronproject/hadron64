metadata = """
summary @ Fast, easy, and free BitTorrent client
homepage @ http://www.transmissionbt.com/ 
license @ MIT 
src_url @ http://mirrors.m0k.org/transmission/files/$name-$version.tar.bz2 
arch @ ~x86
options @ gtk libnotify libcanberra utp
"""

depends = """
runtime @ dev-libs/dbus-glib dev-libs/libevent net-misc/curl dev-util/intltool 
build @ sys-devel/gettext dev-util/intltool dev-util/pkg-config sys-apps/sed
"""

opt_runtime = """
gtk @ x11-libs/gtk+ dev-libs/dbus-glib
    libnotify @ x11-libs/libnotify
    libcanberra @ media-libs/libcanberra
"""

def configure():
	export("CFLAGS", "$CFLAGS -fno-strict-aliasing")
	conf(
	" --disable-gconf2",
	config_enable("gtk"),
	config_enable("utp"),
	config_enable("libcanberra"),
	config_enable("libnotify"))

def install():
	for nav in ("daemon", "cli", "web", "utils", "gtk", "po"):
		raw_install("-C %s DESTDIR=%s" % (bar, install_dir))

	raw_install("-C qt INSTALL_ROOT=%s" % install_dir)

	insdoc("COPYING")

	insfile("qt/transmission-qt.desktop", "/usr/share/applications/transmission-qt.desktop")
	insfile("qt/icons/transmission.png", "/usr/share/pixmaps/transmission-qt.png")
	insfile("%s/transmissiond.conf", "/etc/conf.d/transmissiond")
	insexe("%s/transmissiond", "/etc/rc.d/transmissiond")

def post_install():

#cli icin
	system('echo "If you want to run the Transmission daemon at boot, add transmissiond to the DAEMONS array in /etc/rc.conf. You have to set the user in /etc/conf.d/transmissiond." ')

#gtk icin
	system("gtk-update-icon-cache -q -t -f /usr/share/icons/hicolor")

#qt ve gtk icin
	system("update-desktop-database -q")

