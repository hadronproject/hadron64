metadata = """
summary @ X11 Testing -- Resource extension library
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libXtst-$version.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc x11-libs/libXext x11-proto/recordproto x11-proto/inputproto x11-libs/libXi
build @ x11-misc/util-macros
"""

#srcdir = "libXtst-%s" % version

def configure():
    conf("--disable-static")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    
    insdoc("COPYING")
