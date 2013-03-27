metadata = """
summary @ An open source JPEG 2000 codec 
homepage @ http://www.openjpeg.org 
license @ BSD 
src_url @ http://openjpeg.googlecode.com/files/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ media-libs/libpng media-libs/tiff media-libs/lcms sys-libs/zlib
"""

def prepare():
    patch()

def configure():
    system("rm -fr thirdparty")
    conf("--disable-static")

def install():
    installd()

