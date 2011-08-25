metadata = """
summary @ A collection of routines used to create PNG format graphics files
homepage @ http://www.libpng.org/pub/png/libpng.html
license @ custom
src_url @ http://downloads.sourceforge.net/sourceforge/libpng/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc sys-libs/zlib
"""

#def prepare():
#       patch(level=1)

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("LICENSE")
