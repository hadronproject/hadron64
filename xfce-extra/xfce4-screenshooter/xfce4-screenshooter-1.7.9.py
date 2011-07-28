metadata = """
summary @ Plugin that makes screenshots for the XFCE4 panel
homepage @ http://goodies.xfce.org/projects/applications/xfce4-screenshooter
license @ GPL2
src_url @ http://archive.xfce.org/src/apps/$name/1.7/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ net-libs/libsoup
"""

def prepare():
    patch(level=1)

def configure():
    conf("--disable-static",
            "--disable-debug")

def install():
    raw_install("DESTDIR=%s" % install_dir)

