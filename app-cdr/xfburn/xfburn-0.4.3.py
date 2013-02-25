metadata = """
summary @ A simple CD/DVD burning tool
homepage @ http://goodies.xfce.org/projects/applications/xfburn
license @ GPL-2
src_url @ http://www.xfce.org/archive/src/apps/xfburn/0.4/$fullname.tar.bz2
options @ debug gstreamer
arch @ ~x86_64
"""

depends = """
common @ >=sys-libs/glib-2.22 >=dev-libs/libburn-0.4.2 >=dev-libs/libisofs-0.6.2 >=x11-libs/gtk+-2.10
>=xfce-base/exo-0.6 >=xfce-base/libxfce4ui-4.8
"""

opt_common = """
gstreamer @ media-libs/gst-plugins-base
udev @ sys-fs/udev[gudev]
"""
get("fdo_mime", "gnome2_utils")

prepare = lambda: (patch("xfburn-0.4.3-update_desktop_entry.patch"), patch("fix_empty_dir_segfault.diff"))
install = lambda: installd()

def configure():
    conf(config_enable("udev", "gudev"),
            config_enable("gstreamer"),
            config_enable("debug"),
            "--disable-hal",
            "--enable-dbus")

def post_install():
    desktop_database_update()
    gnome2_icon_cache_update()
