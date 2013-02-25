metadata = """
summary @ Lightweight color management development library/engine
homepage @ http://www.littlecms.com/
license @ custom
src_url @ http://garr.dl.sourceforge.net/project/lcms/lcms/2.2/lcms2-$version.tar.gz
arch @ ~x86_64
options @ jpeg tiff zlib static-libs
"""

opt_runtime = """
jpeg @ media-libs/jpeg
tiff @ media-libs/tiff
zlib @ sys-libs/zlib
"""

srcdir = name + "2-" + version

def configure():
    conf(
    config_enable("static-libs", "static"),
    config_with("jpeg"),
    config_with("tiff"),
    config_with("zlib"))

def install():
    raw_install("DESTDIR=%s" % install_dir)
