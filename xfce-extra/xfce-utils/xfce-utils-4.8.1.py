metadata = """
summary @ Utilities for Xfce
homepage @ http://www.xfce.org/
license @ GPL2
src_url @ http://archive.xfce.org/src/xfce/$name/4.8/$fullname.tar.bz2
arch @ ~x86
options @ dbus
"""

depends = """
runtime @ xfce-base/libxfce4ui x11-misc/xinit x11-themes/hicolor-icon-theme
"""

opt_runtime = """
dbus @ dev-libs/dbus-glib
"""

def configure():
    conf("--disable-static",
            "--enable-dbus",
            "--disable-debug",
            "--with-vendor-info=Hadron",
            config_enable("dbus"))

def install():
    raw_install("DESTDIR=%s" % install_dir)

def post_install():
    system("gtk-update-icon-cache -q -t -f /usr/share/icons/hicolor")
