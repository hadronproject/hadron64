metadata = """
summary @ X11 Video extension library
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libXv-$version.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc x11-proto/videoproto x11-libs/libXext
"""

#srcdir = "libXv-%s" % version

def configure():
	conf(
	"--disable-static")

def install():
	raw_install("DESTDIR=%s" % install_dir)
	
	insdoc("COPYING")
