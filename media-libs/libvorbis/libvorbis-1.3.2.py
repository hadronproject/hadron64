metadata = """
summary @ Vorbis codec library
homepage @ http://www.xiph.org/ogg/vorbis/
license @ custom
src_url @ http://downloads.xiph.org/releases/vorbis/$fullname.tar.gz
arch @ ~x86_64
options @ static-libs
"""

depends = """
runtime @ media-libs/libogg
"""

def configure():
    conf(
    "--disable-dependency-tracking",
    config_enable("static-libs", "static"))

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("AUTHORS", "CHANGES")
