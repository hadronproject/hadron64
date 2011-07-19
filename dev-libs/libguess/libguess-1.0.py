metadata = """
summary @ High-speed character set detection library
homepage @ http://atheme.org/project/libguess
license @ BSD
src_url @ http://distfiles.atheme.org/$fullname.tgz
arch @ ~x86
options @ examples
"""

depends = """
runtime @ dev-libs/libmowgli
build @ dev-util/pkg-config
"""

def configure():
	conf(
	config_enable("examples"))

def install():
	raw_install("DESTDIR=%s" % install_dir)
	
	insdoc("README")
