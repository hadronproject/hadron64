metadata = """
summary @ Ristretto is a image viewer for XFCE4
homepage @ http://goodies.xfce.org/projects/applications/ristretto
license @ GPL2
src_url @ http://archive.xfce.org/src/apps/$name/0.0/$fullname.tar.bz2
arch @ ~x86
options @ debug
"""

depends = """
runtime @ xfce-base/libxfce4ui dev-util/desktop-file-utils
          x11-themes/hicolor-icon-theme media-libs/libexif
"""


def configure():
    conf(
    config_enable("debug"),
    )

def install():
    raw_install("DESTDIR=%s" % install_dir)

def post_install():
    system("update-desktop-database -q")
    system("gtk-update-icon-cache -q -t -f /usr/share/icons/hicolor")
