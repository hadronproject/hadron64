metadata = """
summary @ X11 pixmap library
homepage @ http://xorg.freedesktop.org/
license @ MIT
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libXpm-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc x11-libs/libXt x11-libs/libXext
build @ x11-misc/util-macros
"""

def configure():
    conf(
    "--disable-static")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("COPYING")
