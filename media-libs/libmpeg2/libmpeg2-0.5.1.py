metadata = """
summary @ libmpeg2 is a library for decoding MPEG-1 and MPEG-2 video streams
homepage @ http://libmpeg2.sourceforge.net/
license @ GPL2
src_url @ http://libmpeg2.sourceforge.net/files/$fullname.tar.gz
arch @ ~x86
options @ X sdl
"""


opt_runtime = """
X @ x11-libs/libXv x11-libs/libICE x11-libs/libSM x11-libs/libXt
sdl @ media-libs/SDL
"""

opt_build = """
X @ x11-proto/xextproto
"""

def configure():
    conf(
    "--enable-shared",
    "--disable-dependency-tracking",
    config_enable("X", "x"),
    config_enable("sdl"))

def build():
    make('OPT_CFLAGS="${CFLAGS}" \
    MPEG2DEC_CFLAGS="${CFLAGS}" \
    LIBMPEG2_CFLAGS=""')

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("AUTHORS", "ChangeLog", "NEWS", "README", "TODO")
