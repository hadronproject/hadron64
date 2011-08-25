metadata = """
summary @ Library that does image file loading and saving as well as rendering, manipulation, arbitrary polygon support
homepage @ http://sourceforge.net/projects/enlightenment/
license @ BSD
src_url @ http://downloads.sourceforge.net/enlightenment/$fullname.tar.bz2
arch @ ~x86
options @ bzip2 gif jpeg mp3 png tiff zlib X
"""

depends = """
runtime @ media-libs/freetype
"""

opt_runtime = """
tiff @ media-libs/tiff
gif @ media-libs/giflib
bzip2 @ app-arch/bzip2
X @ x11-libs/libXext x11-proto/xextproto
png @ media-libs/libpng
jpeg @ media-libs/jpeg
mp3 @ media-libs/libid3tag
zlib @ sys-libs/zlib
"""

def prepare():
    patch()

def configure():
    conf(
    "--prefix=/usr",
    "--sysconfdir=/etc/imlib2",
    "--x-libraries=/usr/lib",
    "--disable-mmx",
    config_with("X", "x"),
    config_with("jpeg"),
    config_with("png"),
    config_with("tiff"),
    config_with("gif"),
    config_with("zlib"),
    config_with("bzip2"),
    config_with("mp3", "id3"))

def install():
    raw_install("DESTDIR=%s" % install_dir)
