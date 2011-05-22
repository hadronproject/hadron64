metadata = """
summary @ Window manager for the Xfce desktop environment
homepage @ http://www.xfce.org/
license @ GPL2
src_url @ http://archive.xfce.org/src/xfce/$name/4.8/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ xfce-base/libxfce4ui x11-libs/libwnck x11-themes/hicolor-icon-theme
"""

def configure():
    conf("--disable-static"
            "--enable-startup-notification"
            "--enable-randr"
            "--enable-compositor"
            "--enable-xsync"
            "--disable-debug")

def install():
    raw_install("DESTDIR=%s" % install_dir)

