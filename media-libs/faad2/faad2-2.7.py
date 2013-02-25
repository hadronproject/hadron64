metadata = """
summary @ ISO AAC audio decoder
homepage @ http://www.audiocoding.com/
license @ custom:GPL
src_url @ http://downloads.sourceforge.net/sourceforge/faac/$name-$version.tar.bz2
arch @ ~x86_64
options @ digitalradio static-libs
"""

depends = """
runtime @ sys-libs/glibc
"""

def configure():
    conf(
    config_enable("static-libs", "static"),
    config_enable("digitalradio", "drm"),
    "--without-xmms",
    "--disable-dependency-tracking")

def install():
    raw_install("DESTDIR=%s manmdir=/usr/share/man/man1" % install_dir)

    insfile("common/mp4ff/mp4ff_int_types.h", "/usr/include/mp4ff_int_types.h")

    insdoc("AUTHORS", "ChangeLog", "NEWS", "README", "README.linux", "TODO")
