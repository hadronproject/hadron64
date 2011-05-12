metadata = """
summary @ X11 Athena Widget library
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libXaw-$version.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc x11-libs/libXmu x11-libs/libXpm
build @ x11-misc/util-macros
"""

#srcdir = "libXaw-%s" % version

def configure():
	conf(
	"--disable-static")

def install():
	raw_install("DESTDIR=%s" % install_dir)
	
	insdoc("COPYING")
