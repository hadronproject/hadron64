metadata = """
summary @ Property displayer for X
homepage @ http://xorg.freedesktop.org/
license @ MIT
src_url @ http://xorg.freedesktop.org/archive/individual/app/xprop-$version.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc x11-libs/libX11
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
