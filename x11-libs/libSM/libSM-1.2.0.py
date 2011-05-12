metadata = """
summary @ X11 Session Management library
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libSM-$version.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ x11-libs/libICE sys-apps/util-linux
build @ x11-misc/util-macros x11-libs/xtrans
"""

#srcdir = "libSM-%s" % version

def install():
	raw_install("DESTDIR=%s" % install_dir)
	
	insdoc("COPYING")
