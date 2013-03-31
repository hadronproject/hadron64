metadata = """
summary @ XFCE4 Volume Control
homepage @ http://www.xfce.org/
license @ GPL2
src_url @ http://archive.xfce.org/src/apps/$name/4.10/$fullname.tar.bz2
arch @ ~x86_64
options @ debug
"""


depends = """
common @ dev-libs/libunique:1 media-plugins/gst-plugins-base:0 xfce-base/xfce4-panel
build @ dev-util/intltool
"""

def configure():
    conf("--disable-static",
    config_enable("debug"))

def install():
    install()

def post_install():
    system("gtk-update-icon-cache -q -t -f /usr/share/icons/hicolor")
