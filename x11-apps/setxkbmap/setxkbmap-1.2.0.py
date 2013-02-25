metadata = """
summary @ Set the keyboard using the X Keyboard Extension
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/app/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/libxkbfile x11-libs/libX11
build @ x11-misc/util-macros
"""

def configure():
    conf(
    "--prefix=/usr")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
