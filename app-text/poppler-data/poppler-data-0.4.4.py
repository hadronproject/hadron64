metadata = """
summary @ Encoding data for the poppler PDF rendering library 
homepage @ http://poppler.freedesktop.org/ 
license @ custom GPL2 
src_url @ http://poppler.freedesktop.org/$name-$version.tar.gz 
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
"""

def configure():
	pass

def build():
	pass

def install():
	raw_install("DESTDIR=%s prefix=/usr" % install_dir)

	insdoc("COPYING")
	insdoc("COPYING.adobe")

