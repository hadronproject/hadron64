metadata = """
summary @ An open source JPEG 2000 codec 
homepage @ http://www.openjpeg.org 
license @ BSD 
src_url @ http://openjpeg.googlecode.com/files/openjpeg_v1_4_sources_r697.tgz 
arch @ ~x86
"""

depends = """
runtime @ media-libs/libpng media-libs/tiff media-libs/lcms sys-libs/zlib
"""

srcdir = "openjpeg_v1_4_sources_r697"

def prepare():
    patch(level=1)
    system("sed -i -e 's:LICENSE::g' CMakeLists.txt")

def configure():
	system("rm -fr libs")
	conf(
	"--disable-static")

def build():
	make(j=1)

def install():
	raw_install("DESTDIR=%s" % install_dir)


#build hatali
