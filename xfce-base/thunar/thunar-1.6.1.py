metadata = """
summary @ File manager for the Xfce desktop environment
homepage @ http://thunar.xfce.org
license @ GPL2 LGPL2.1
src_url @ http://archive.xfce.org/src/xfce/$name/1.6/Thunar-$version.tar.bz2
arch @ ~x86_64
options @ dbus libnotify pcre startup-notification udev debug
"""

depends ="""
common @ >=dev-lang/perl-5.6 >=sys-libs/glib-2.30 >=x11-libs/gdk-pixbuf-2.14 >=x11-libs/gtk+-2.24:2
>=xfce-base/exo-0.10 >=xfce-base/libxfce4ui-4.10 >=xfce-base/libxfce4util-4.10 >=xfce-base/xfconf-4.10
sys-apps/systemd
"""

opt_common="""
dbus @ >=dev-libs/dbus-glib-0.100
exif @ >=media-libs/libexif-0.6.19
libnotify @ >=x11-libs/libnotify-0.7
pcre @ >=dev-libs/libpcre-6
startup-notification @ x11-libs/startup-notification
"""

srcdir = "Thunar-%s" % version

get("gnome2_utils", "fdo_mime")

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
            config_enable("debug"))

def install():
    raw_install("DESTDIR=%s" % install_dir)

def post_install():
    desktop_database_update()
    gnome2_icon_cache_update()
