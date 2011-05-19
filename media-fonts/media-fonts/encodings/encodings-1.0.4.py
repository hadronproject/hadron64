metadata = """
summary @ X.org font encoding files
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/font/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc
build @ x11-apps/mkfontscale x11-misc/util-macros media-fonts/font-util
"""

def configure():
	autoreconf()
	conf()

def install():
	raw_install("DESTDIR=%s" % install_dir)
	
	insdoc("COPYING")
