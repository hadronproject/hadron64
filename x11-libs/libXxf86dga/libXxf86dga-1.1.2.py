metadata = """
summary @ X11 Direct Graphics Access extension library
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libXxf86dga-$version.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc x11-libs/libXext x11-proto/xf86dgaproto
"""

#srcdir = "libXxf86dga-%s" % version

def configure():
	conf(
	"--disable-static")

def install():
	raw_install("DESTDIR=%s" % install_dir)
	
	insdoc("COPYING")
