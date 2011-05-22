metadata = """
summary @ XFCE4 Application Finder
homepage @ http://www.xfce.org/
license @ GPL2
src_url @ http://archive.xfce.org/src/xfce/$name/4.8/$fullname.tar.bz2
arch @ ~x86
"""


depends = """
runtime @ xfce-base/libxfce4ui xfce-base/garcon x11-themes/hicolor-icon-theme
"""

def configure():
    conf("--disable-static",
            "--disable-debug")

def install():
    raw_install("DESTDIR=%s" % install_dir)

def post_install():
    system("gtk-update-icon-cache -q -t -f /usr/share/icons/hicolor")
