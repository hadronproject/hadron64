metadata = """
summary @ A high-quality MPEG audio decoder
homepage @ http://www.underbit.com/products/mad/
license @ GPL
src_url @ http://downloads.sourceforge.net/sourceforge/mad/$fullnameb.tar.gz
arch @ ~x86
options @ debug
"""

depends = """
runtime @ sys-libs/glibc
"""

srcdir = fullname+"b"

def prepare():
	patch(level=1)

def configure():
    autoconf()
    conf(
    "--enable-fpm=intel",
	"--enable-accuracy",
	config_enable("debug", "debugging"))

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("CHANGES", "CREDITS", "README", "TODO", "VERSION")
