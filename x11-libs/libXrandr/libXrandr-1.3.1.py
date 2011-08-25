metadata = """
summary @ X11 RandR extension library
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libXrandr-$version.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ x11-libs/libXext x11-libs/libXrender x11-proto/randrproto
build @ x11-misc/util-macros
"""

#srcdir = "libXrandr-%s" % version

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
