metadata = """
summary @ X11 Video Motion Compensation extension library
homepage @ http://xorg.freedesktop.org/
license @ MIT
src_url @ http://xorg.freedesktop.org/releases/individual/lib/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ x11-libs/libXv
build @ dev-util/pkg-config
"""

def configure():
    conf(
    "--prefix=/usr --sysconfdir=/etc --disable-static")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
