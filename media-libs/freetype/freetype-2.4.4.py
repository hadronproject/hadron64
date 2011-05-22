metadata = """
summary @ TrueType font rendering library
homepage @ http://freetype.sourceforge.net/
license @ GPL
src_url @ http://downloads.sourceforge.net/sourceforge/freetype/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc sys-libs/zlib
"""

def prepare():
    patch(level=1)

def install():
    raw_install("DESTDIR=%s" % install_dir)
