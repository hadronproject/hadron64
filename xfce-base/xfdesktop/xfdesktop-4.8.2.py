metadata = """
summary @ A desktop manager for Xfce
homepage @ http://www.xfce.org/
license @ GPL2
src_url @ http://archive.xfce.org/src/xfce/$name/4.8/$fullname.tar.bz2
arch @ ~x86
options @ libnotify thunar debug
"""

depends = """
runtime @ xfce-base/libxfce4ui x11-themes/hicolor-icon-theme x11-libs/libwnck x11-libs/libX11
build @ xfce-base/xfce4-panel dev-util/intltool
"""

opt_runtime = """
thunar @ xfce-base/thunar dev-libs/dbus-glib xfce-base/exo
libnotify @ x11-libs/libnotify
"""

def configure():
    conf("--disable-static",
            "--enable-gio-unix",
            config_enable("thunar", "thunarx"),
            "--enable-exo",
            config_enable("notify", "notifications"),
            config_enable("debug"))

def install():
    raw_install("DESTDIR=%s" % install_dir)

def post_install():
    system("gtk-update-icon-cache -q -t -f /usr/share/icons/hicolor")

