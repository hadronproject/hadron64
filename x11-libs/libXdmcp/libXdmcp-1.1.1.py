metadata = """
summary @ X11 Display Manager Control Protocol library
homepage @ http://xorg.freedesktop.org/
license @ MIT
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libXdmcp-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc x11-proto/xproto
build @ x11-misc/util-macros
"""

#srcdir = "libXdmcp-%s" % version

def configure():
    conf("--disable-static")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
