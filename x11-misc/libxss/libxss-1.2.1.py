metadata = """
summary @ X11 Screen Saver extension library
homepage @ http://xorg.freedesktop.org/ 
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libXScrnSaver-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc x11-libs/libXext x11-proto/scrnsaverproto
"""

srcdir = "libXScrnSaver-%s" % version

def install():
	raw_install("DESTDIR=%s" % install_dir)
	
	insdoc("COPYING")
