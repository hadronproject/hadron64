metadata = """
summary @ A port of Xfce engine to GTK+-2.0
homepage @ http://www.xfce.org/
license @ GPL2
src_url @ http://archive.xfce.org/src/xfce/$name/2.8/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ x11-libs/gtk+
build @ dev-util/pkg-config
"""

def configure():
    conf("--disable-static",
            "--disable-debug")

def install():
    raw_install("DESTDIR=%s" % install_dir)
