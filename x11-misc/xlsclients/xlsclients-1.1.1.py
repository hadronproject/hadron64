metadata = """
summary @ List client applications running on a display
homepage @ http://xorg.freedesktop.org/ 
license @ custom
src_url @ http://xorg.freedesktop.org/archive/individual/app/xlsclients-$version.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc x11-libs/libxcb x11-misc/xcb-util
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)
    
    insdoc("COPYING")
