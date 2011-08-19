metadata = """
summary @ The library for xine-dvdnav plugin
homepage @ http://www.mplayerhq.hu/MPlayer/releases/dvdnav/
license @ GPL
src_url @ http://www.mplayerhq.hu/MPlayer/releases/dvdnav/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ media-libs/libdvdread
"""

def prepare():
	patch(level=1)

def configure():
	system("./autogen.sh --prefix=/usr")
	pass

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("AUTHORS", "DEVELOPMENT-POLICY.txt", "ChangeLog", "TODO", "doc/dvd_structures", "README")
