metadata = """
summary @ X11 damaged region extension library
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libXdamage-$version.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc x11-libs/libXfixes x11-proto/damageproto
"""

#srcdir = "libXdamage-%s" % version

def configure():
    conf("--disable-static")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    
    insdoc("COPYING")
