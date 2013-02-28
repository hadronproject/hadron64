metadata = """
summary @ A collection of routines used to create PNG format graphics files (just for 1.4 compatibility)
homepage @ http://www.libpng.org/pub/png/libpng.html
license @ custom
src_url @ http://downloads.sourceforge.net/sourceforge/libpng/$fullname.tar.bz2
http://garr.dl.sourceforge.net/project/libpng-apng/libpng14/1.4.12/libpng-1.4.12-apng.patch.gz
options @ apng
arch @ ~x86_64
slot @ 1.4
"""

depends = """
runtime @ sys-libs/glibc sys-libs/zlib
"""

def prepare():
    if opt("apng"):
        patch("%s/../libpng-1.4.12-apng.patch" % build_dir, level=1)
        libtoolize()

def configure():
    conf("--disable-static")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("LICENSE")
