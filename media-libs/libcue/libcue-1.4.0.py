metadata = """
summary @ Parses so-called cue sheets and handles the parsed data
homepage @ http://sourceforge.net/projects/libcue/
license @ GPL2
src_url @ http://downloads.sourceforge.net/libcue/$fullname.tar.bz2
arch @ ~x86
options @ static-libs
"""

depends = """
build @ sys-devel/flex
"""

def configure():
	system("./autogen.sh --prefix=/usr",
	config_enable("static-libs", "static"))
	pass

def install():
	raw_install("DESTDIR=%s" % install_dir)

