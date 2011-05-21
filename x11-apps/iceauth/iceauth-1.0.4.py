metadata = """
summary @ ICE authority file utility
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/archive/individual/app/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ x11-libs/libICE
build @ x11-misc/util-macros x11-proto/xproto
"""

def install():
	raw_install("DESTDIR=%s" % install_dir)
	
	insdoc("COPYING")
