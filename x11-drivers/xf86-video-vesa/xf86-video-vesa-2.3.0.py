metadata = """
summary @ X.org vesa video driver
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/driver/$fullname.tar.bz2
arch @ ~x86
options @ debug
"""

depends = """
runtime @ sys-libs/glibc
build @ dev-util/pkg-config x11-base/xorg-server x11-proto/fontsproto x11-proto/randrproto x11-proto/renderproto x11-proto/xextproto x11-proto/xproto
"""

def configure():
	conf(
	"--prefix=/usr")

def install():
	raw_install("DESTDIR=%s" % install_dir)

	insdoc("COPYING")

