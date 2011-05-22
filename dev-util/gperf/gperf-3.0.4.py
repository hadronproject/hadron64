metadata = """
summary @ Perfect hash function generator.
homepage @ http://www.gnu.org/software/gperf/
license @ GPL3
src_url @ ftp://ftp.gnu.org/gnu/gperf/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc sys-apps/texinfo
"""

def install():
	raw_install("DESTDIR=%s" % install_dir)

