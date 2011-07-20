metadata = """
summary @ An implemenation of the Dirac video codec in ANSI C code 
homepage @ http://www.diracvideo.org/ 
license @ GPL2 LGPL2 MPL MIT 
src_url @ http://www.diracvideo.org/download/schroedinger/$name-$version.tar.gz 
arch @ ~x86
"""

depends = """
runtime @ dev-lang/orc
"""

def configure():
    conf(
    "--disable-dependency-tracking")

def build():
	export("HOME", build_dir)
	make()

def install():
	export("HOME", build_dir)
	raw_install("DESTDIR=%s" % install_dir)

	insdoc("AUTHORS", "NEWS", "README", "TODO")

