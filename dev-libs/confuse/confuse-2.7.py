metadata = """
summary @ C-library for parsing configuration files
homepage @ http://www.nongnu.org/confuse
license @ LGPL
src_url @ http://savannah.nongnu.org/download/$name/$fullname.tar.gz
arch @ ~x86
options @ nls static-libs
"""

depends = """
runtime @ sys-devel/flex sys-devel/libtool dev-util/pkg-config
"""

opt_build = """
nls @ sys-devel/gettext
"""

def configure():
	conf(
	config_enable("nls"),
	config_enable("static-libs", "static"),
	"--disable-examples",
	"--enable-shared")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("AUTHORS", "NEWS", "README")
