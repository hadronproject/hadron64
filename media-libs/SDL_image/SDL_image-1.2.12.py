metadata = """
summary @ A simple library to load images of various formats as SDL surfaces
homepage @ http://www.libsdl.org/projects/SDL_image/
license @ LGPL
src_url @ http://www.libsdl.org/projects/SDL_image/release/$fullname.tar.gz
arch @ ~x86_64
options @ gif jpeg png static-libs tiff
"""

depends = """
common @ >=media-libs/SDL-1.2.13 sys-libs/zlib
"""
opt_runtime = """
png @ media-libs/libpng
jpeg @ media-libs/jpeg
tiff @ media-libs/tiff
"""

def configure():
    conf(
    "--disable-jpg-shared",
    "--disable-png-shared",
    "--disable-tif-shared",
    config_enable("static-libs", "static"),
    config_enable("gif"),
    config_enable("jpeg", "jpg"),
    config_enable("tiff", "tif"),
    config_enable("png"),
    "--enable-bmp",
    "--enable-lbm",
    "--enable-pcx",
    "--enable-pnm",
    "--enable-tga",
    "--enable-xcf",
    "--enable-xpm",
    "--enable-xv")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("CHANGES", "README")
