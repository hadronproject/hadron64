metadata = """
summary @ File manager for the Xfce desktop environment
homepage @ http://thunar.xfce.org
license @ GPL2 LGPL2.1
src_url @ http://archive.xfce.org/src/xfce/$name/1.2/Thunar-$version.tar.bz2
arch @ ~x86
options @ dbus libnotify pcre startup-notification udev
"""

depends = """
runtime @ xfce-base/exo sys-libs/glib x11-libs/gtk+:2 xfce-base/libxfce4util xfce-base/libxfce4ui
    dev-lang/perl x11-misc/shared-mime-info dev-util/desktop-file-utils
build @ dev-util/intltool dev-util/pkg-config sys-devel/gettext
"""

opt_runtime = """
dbus @ dev-libs/dbus-glib
libnotify @ x11-libs/libnotify
pcre @ dev-libs/pcre
startup-notification @ x11-libs/startup-notification
udev @ sys-fs/udev
pcre @ dev-libs/pcre
"""


srcdir = "Thunar-%s" % version

def configure():
    conf("--disable-static",
            "--enable-gio-unix",
            config_enable("dbus"),
            config_enable("startup-notification"),
            config_enable("udev", "gudev"),
            config_enable("libnotify", "notifications"),
            "--enable-exif",
            config_enable("pcre"),
            "--disable-gtk-doc",
            "--disable-debug")

def install():
    raw_install("DESTDIR=%s" % install_dir)

def post_install():
    system("update-desktop-database -q")
    system("gtk-update-icon-cache -q -t -f /usr/share/icons/hicolor")
