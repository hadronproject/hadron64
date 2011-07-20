metadata = """
summary @ VDPAU backend for VA API 
homepage @ http://www.splitted-desktop.com/~gbeauchesne/vdpau-video/ 
license @ GPL 
src_url @ http://www.splitted-desktop.com/~gbeauchesne/vdpau-video/$name-$version.tar.gz 
arch @ ~x86
"""

depends = """
runtime @ x11-libs/libvdpau
build @ media-libs/mesa
"""

def install():
	raw_install("DESTDIR=%s" % install_dir)

