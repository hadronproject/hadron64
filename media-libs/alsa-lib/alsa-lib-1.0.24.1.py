metadata = """
summary @ An alternative implementation of Linux sound support
homepage @ http://www.alsa-project.org/
license @ GPL
src_url @ ftp://ftp.alsa-project.org/pub/lib/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc
"""

def configure():
	conf(
	"--with-pythonlibs=\"-lpthread -lm -ldl -lpython2.7\" --with-pythonincludes=-I/usr/include/python2.7")

def install():
	raw_install("DESTDIR=%s" % install_dir)

