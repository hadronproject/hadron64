metadata = """
summary @ A battery monitor plugin for the Xfce panel 
homepage @ http://xfce-goodies.berlios.de/ 
license @ GPL2 
src_url @ http://archive.xfce.org/src/panel-plugins/$name/1.0/$fullname.tar.bz2
arch @ ~x86
options @ debug
"""

depends = """
runtime @ xfce-base/xfce4-panel xfce-base/libxfcegui4 x11-themes/hicolor-icon-theme 
build @ dev-util/intltool
"""

def configure():
    conf(
    "--sysconfdir=/etc",
    "--libexecdir=/usr/lib",
    "--localstatedir=/var",
    "--disable-static",
	config_enable("debug"))

def install():
	raw_install("DESTDIR=%s" % install_dir)


def post_install():
	system("gtk-update-icon-cache -q -t -f /usr/share/icons/hicolor")
