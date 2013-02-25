metadata = """
summary @ Window manager for the Xfce desktop environment
homepage @ http://www.xfce.org/
license @ GPL2
src_url @ http://archive.xfce.org/src/xfce/$name/4.8/$fullname.tar.bz2
arch @ ~x86_64
options @ startup-notification
"""

depends = """
runtime @ xfce-base/libxfce4util xfce-base/libxfce4ui x11-libs/libwnck x11-themes/hicolor-icon-theme
    xfce-base/xfconf sys-libs/glib x11-libs/gtk+:2 x11-libs/libICE x11-libs/libSM x11-libs/libX11
    x11-libs/libXext x11-libs/libXrandr x11-libs/libXrender media-libs/pango
    x11-libs/libXcomposite x11-libs/libXdamage x11-libs/libXfixes
build @ dev-util/intltool dev-util/pkg-config sys-devel/gettext
"""

opt_runtime = """
startup-notification @ x11-libs/startup-notification
"""

def configure():
    conf("--disable-static",
            config_enable("startup-notification"),
            "--enable-randr",
            "--enable-compositor",
            "--enable-xsync",
            "--disable-debug")

def install():
    raw_install("DESTDIR=%s" % install_dir)
