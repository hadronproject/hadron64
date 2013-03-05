metadata = """
summary @ X11 Xinerama extension library
homepage @ http://xorg.freedesktop.org/
license @ MIT
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libXinerama-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/libXext x11-proto/xineramaproto
build @ x11-misc/util-macros
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
