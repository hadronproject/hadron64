metadata = """
summary @ Settings manager for XFCE4
homepage @ http://www.xfce.org/
license @ GPL2
src_url @ http://archive.xfce.org/src/xfce/$name/4.8/$fullname.tar.bz2
arch @ ~x86
options @ debug libnotify
"""

depends = """
runtime @ x11-libs/libXcursor x11-libs/gtk+ sys-libs/glib dev-libs/dbus-glib
    x11-libs/libXi x11-libs/libXrandr xfce-base/libxfce4util xfce-base/libxfce4ui
    xfce-base/xfconf xfce-base/exo
build @ x11-proto/inputproto sys-devel/gettext dev-util/pkg-config dev-util/intltool
"""

opt_runtime = """
libnotify @ x11-libs/libnotify
"""

def prepare():
    patch(level=1)

def configure():
    conf("--disable-static",
            "--enable-xrandr",
            "--enable-xcursor",
            config_enable("libnotify"),
            "--enable-libxklavier",
            "--enable-pluggable-dialogs",
            config_enable("debug"))

def install():
    raw_install("DESTDIR=%s" % install_dir)
