metadata = """
summary @ X11 miscellaneous micro-utility library
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libXmu-$version.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc x11-libs/libXext x11-libs/libXt
build @ x11-misc/util-macros
"""

#srcdir = "libXmu-%s" % version

def configure():
	conf(
	"--disable-static")

def install():
	raw_install("DESTDIR=%s" % install_dir)
	
	insdoc("COPYING")
