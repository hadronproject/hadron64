metadata = """
summary @ X.org evdev input driver
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/driver/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
build @ x11-libs/libXext x11-libs/libXfixes x11-libs/libXvMC >=x11-libs/libxcb-1.5
"""

def configure():
    conf("--enable-dri", "--enable-xvmc")
def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
