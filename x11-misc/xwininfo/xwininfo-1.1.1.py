metadata = """
summary @ rints out the capabilities of any video adaptors associated with the display that are accessible through the X-Video extension
homepage @ http://xorg.freedesktop.org/ 
license @ custom
src_url @ http://xorg.freedesktop.org/archive/individual/app/xvinfo-$version.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc x11-libs/libX11 x11-libs/libXv
"""


def install():
    raw_install("DESTDIR=%s" % install_dir)
    
    insdoc("COPYING")
