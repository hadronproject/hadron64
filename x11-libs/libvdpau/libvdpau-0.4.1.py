metadata = """
summary @ Nvidia VDPAU library
homepage @ http://cgit.freedesktop.org/~aplattner/libvdpau
license @ MIT
src_url @ http://people.freedesktop.org/~aplattner/vdpau/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-devel/gcc
build @ x11-libs/libX11
"""

def configure():
	conf(
	"--disable-dependency-tracking")

def install():
	raw_install("DESTDIR=%s" % install_dir)
	
	insdoc("AUTHORS", "ChangeLog")
