metadata = """
summary @ Cairo vector graphics library
homepage @ http://cairographics.org/
license @ LGPL + MPL
src_url @ http://cairographics.org/releases/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ media-libs/libpng x11-libs/libXrender media-libs/fontconfig
          x11-libs/pixman sys-libs/glib media-libs/freetype sys-libs/zlib

"""

def prepare():
    patch(level=1)

def configure():
    conf("--disable-static",
            "--enable-tee",
            "--enable-gl")

def install():
    raw_install("DESTDIR=%s" % install_dir)
