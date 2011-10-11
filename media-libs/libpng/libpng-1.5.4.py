metadata = """
summary @ A collection of routines used to create PNG format graphics files
homepage @ http://www.libpng.org/pub/png/libpng.html
license @ custom
src_url @ http://downloads.sourceforge.net/sourceforge/libpng/$fullname.tar.bz2  
http://garr.dl.sourceforge.net/project/libpng-apng/libpng-devel/1.5.4/libpng-1.5.4-apng.patch.gz
options @ apng
arch @ ~x86
slot @ 1.5
"""

depends = """
runtime @ sys-libs/glibc sys-libs/zlib
"""

def prepare():
    if opt("apng"):
        patch("libpng-1.5.4-apng.patch", level=1)
        libtoolize()

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("LICENSE")
