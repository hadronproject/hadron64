metadata = """
summary @ free library for encoding H264/AVC video streams
homepage @ http://www.videolan.org/developers/x264.html
license @ GPL
src_url @ ftp://ftp.videolan.org/pub/videolan/x264/snapshots/x264-snapshot-$version-2245.tar.bz2
arch @ ~x86
options @ threads pic debug
"""

depends = """
runtime @ sys-libs/glibc
build @ dev-lang/yasm
"""

srcdir = name+"-snapshot-"+version+"-2245"

def configure():
    myconf = ""
    if opt("pic"):
        myconf += " --disable-asm "

    conf(
    config_enable("threads", "thread"),
    "--disable-avs",
    "--disable-lavf",
    "--disable-swscale",
    "--disable-gpac",
    "--enable-pic",
    "--enable-shared",
    config_enable("debug"))

def install():
    raw_install("DESTDIR=%s bindir=/usr/bin libdir=/usr/lib includedir=/usr/include" % install_dir)

    insdoc("AUTHORS")
