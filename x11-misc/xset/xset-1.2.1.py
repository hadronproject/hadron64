metadata = """
summary @ User preference utility for X
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/archive/individual/app/xset-$version.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc x11-libs/libXmu
"""

def configure():
    conf("--without-fontcache --without-xf86misc")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    
    insdoc("COPYING")
