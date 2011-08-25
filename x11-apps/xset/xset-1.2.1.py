metadata = """
summary @ User preference utility for X
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/archive/individual/app/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
build @ x11-misc/util-macros
"""

def configure():
    conf("--without-fontcache",
            "--without-xf86misc")


def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
