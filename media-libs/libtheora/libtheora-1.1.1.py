metadata = """
summary @ An open video codec developed by the Xiph.org 
homepage @ http://www.xiph.org 
license @ BSD 
src_url @ http://downloads.xiph.org/releases/theora/libtheora-$version.tar.bz2 
arch @ ~x86_64
options @ encode static-libs
"""

depends = """
runtime @ media-libs/libogg
build @ dev-util/pkg-config
"""

opt_depends = """
encode @ media-libs/libvorbis
"""

def configure():
	conf(
	"--disable-examples",
	"--enable-shared",
	"--disable-dependency-tracking",
	"--disable-spec",
	config_enable("static-libs", "static"),
	config_enable("encode"))

def install():
	raw_install("DESTDIR=%s" % install_dir)

	insdoc("COPYING", "AUTHORS", "README")
