metadata = """
summary @ A desktop manager for Xfce
homepage @ http://www.xfce.org/
license @ GPL2
src_url @ http://archive.xfce.org/src/xfce/$name/4.8/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ xfce-base/libxfce4ui xfce-base/thunar x11-themes/hicolor-icon-theme x11-libs/libwnck
build @ xfce-base/xfce4-panel dev-util/intltool"""

def configure():
    conf("--disable-static",
            "--enable-gio-unix",
            "--enable-thunarx",
            "--enable-exo",
            "--enable-notifications",
            "--disable-debug")

def install():
    raw_install("DESTDIR=%s" % install_dir)

def post_install():
    system("gtk-update-icon-cache -q -t -f /usr/share/icons/hicolor")

