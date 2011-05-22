metadata = """
summary @ Settings manager for XFCE4
homepage @ http://www.xfce.org/
license @ GPL2
src_url @ http://archive.xfce.org/src/xfce/$name/4.8/$fullname.tar.bz2
arch @ ~x86
"""

def prepare():
    patch(level=1)

def configure():
    conf("--disable-static",
            "--enable-xrandr",
            "--enable-xcursor",
            "--enable-libnotify",
            "--enable-libxklavier",
            "--enable-pluggable-dialogs",
            "--disable-debug")

def install():
    raw_install("DESTDIR=%s" % install_dir)

