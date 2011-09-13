metadata = """
summary @ plugin to track time for the Xfce4 panel 
homepage @ http://goodies.xfce.org/projects/panel-plugins/xfce4-timer-plugin
license @ GPL-2
src_url @ http://archive.xfce.org/src/panel-plugins/$name/0.6/$fullname.tar.bz2
arch @ ~x86
options @ debug
"""

depends = """
runtime @ xfce-base/xfce4-panel xfce-base/libxfcegui4 x11-themes/hicolor-icon-theme 
build @ dev-util/intltool
"""

def prepare():
    patch("panel48.patch", level=1)

def configure():
    conf(
    "--sysconfdir=/etc",
    "--libexecdir=/usr/lib",
    "--localstatedir=/var",
    "--disable-static",
	config_enable("debug"))

def install():
	raw_install("DESTDIR=%s" % install_dir)
