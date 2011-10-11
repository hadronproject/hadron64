metadata = """
summary @ A library for reading and writing gif images
homepage @ http://sourceforge.net/projects/giflib/
license @ MIT
src_url @ http://downloads.sourceforge.net/sourceforge/giflib/$fullname.tar.bz2
arch @ ~x86
options @ X static-libs
"""

opt_runtime = """
X @ x11-libs/libXt x11-libs/libX11 x11-libs/libICE x11-libs/libSM
"""

def configure():
	conf(
	config_enable("static-libs", "static"),
	config_enable("X", "x11"),
	"--disable-gl",
	"--disable-rle")

def install():
	raw_install("DESTDIR=%s" % install_dir)
	
	insdoc("AUTHORS", "BUGS", "ChangeLog", "NEWS", "ONEWS", "README", "TODO", "doc/*.txt")

