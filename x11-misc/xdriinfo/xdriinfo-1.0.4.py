metadata = """
summary @ Query configuration information of DRI drivers
homepage @ http://xorg.freedesktop.org/ 
license @ custom
src_url @ http://xorg.freedesktop.org/archive/individual/app/xdriinfo-$version.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc x11-libs/libX11 media-libs/mesa
build @ x11-proto/glproto media-libs/mesa 
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)
    
    insdoc("COPYING")
