metadata = """
summary @ Library for manipulation of TIFF images
homepage @ http://www.remotesensing.org/libtiff/
license @ custom
src_url @ ftp://ftp.remotesensing.org/pub/libtiff/tiff-$version.tar.gz
arch @ ~x86_64
options @ jpeg lzma
"""

depends = """
runtime @ sys-libs/glibc sys-libs/zlib
build @ media-libs/freeglut x11-libs/libXi x11-libs/libXmu media-libs/mesa
"""

opt_runtime = """
jpeg @ media-libs/jpeg
lzma @ app-arch/xz
"""

def configure():
    conf(config_enable("lzma"),
            config_enable("jpeg"))

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYRIGHT")
