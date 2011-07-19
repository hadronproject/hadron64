metadata = """
summary @ GNU Compact Disc Input and Control Library
homepage @ http://www.gnu.org/software/libcdio/
license @ GPL3
src_url @ http://ftp.gnu.org/gnu/libcdio/$fullname.tar.gz
arch @ ~x86
options @ static-libs cddb
"""

depends = """
build @ dev-util/pkg-config sys-devel/gettext
"""

opt_runtime = """
cddb @ media-libs/libcddb
"""

def configure():
	conf(
	"--disable-vcd-info --enable-cpp-progs",
	config_enable("static-libs", "static"),
	config_enable("cddb"))

def install():
	raw_install("DESTDIR=%s" % install_dir)

#def post_install():
#	system("install-info /usr/share/info/libcdio.info.gz /usr/share/info/dir 2> /dev/null")
