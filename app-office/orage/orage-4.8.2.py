metadata = """
summary @ Xfce's calendar suite (with panel plug-in)
homepage @ http://www.xfce.org/projects/orage/
license @ GPL-2
src_url @ http://archive.xfce.org/src/apps/$name/4.8/$fullname.tar.bz2
options @ dbus libnotify debug plugin berkdb
arch @ ~x86
"""

depends = """
common @ >=dev-libs/libical-0.43
dev-libs/popt
>=x11-libs/gtk+-2.10:2
"""

opt_common = """
berkdb @ sys-libs/db
dbus @ >=dev-libs/dbus-glib-0.88
libnotify @ >=x11-libs/libnotify-0.4.5
xfce_plugins_clock @ >=xfce-base/xfce4-panel-4.8
"""

get("gnome2_utils", "fdo_mime")

def configure():
    conf("--enable-libical",
            config_enable("plugin", "libxfce4panel"),
            config_enable("dbus"),
            config_enable("libnotify"),
            config_with("berkdb", "bdb4"),
            config_enable("debug"))

def install():
    raw_install("-j1 DESTDIR=%s" % install_dir)
    insdoc("AUTHORS", "ChangeLog", "NEWS", "README", "TODO")

def post_install():
    gnome2_icon_cache_update()
    desktop_database_update()
