metadata = """
summary @ Graph based image processing framework
homepage @ http://www.gegl.org/
license @ GPL3 LGPL3
src_url @ http://mirror.csclub.uwaterloo.ca/gentoo-distfiles/distfiles/$fullname.tar.bz2
arch @ ~x86_64
options @ cairo exif ffmpeg graphviz jpeg jpeg2k lua openexr png sdl svg debug mmx sse
"""

depends = """
runtime @ >=media-libs/babl-0.1.4 sys-libs/glib x11-libs/gtk+:2 x11-libs/gdk-pixbuf
media-libs/pango sys-libs/zlib
"""

opt_runtime = """
cairo @ x11-libs/cairo
exif @ media-gfx/exiv2
ffmpeg @ media-video/ffmpeg
jpeg @ media-libs/jpeg
jpeg2k @ media-libs/jasper
lua @ dev-lang/lua
openexr @ media-libs/openexr
png @ media-libs/libpng
sdl @ media-libs/SDL
svg @ gnome-base/librsvg
"""

#TODO: more options http://znurt.org/media-libs/gegl/gegl-0.1.6

def prepare():
    patch(level=1)

def configure():
    conf(
    config_enable("mmx"),
    config_enable("sse"),
    config_enable("debug"),
    config_with("cairo"),
    config_with("cairo", "pangocairo"),
    config_with("exif", "exiv2"),
    config_with("ffmpeg", "libavformat"),
    config_with("graphviz"),
    config_with("jpeg", "libjpeg"),
    config_with("jpeg2k", "jasper"),
    config_with("lua"),
    config_with("openexr"),
    config_with("png", "libpng"),
    config_with("sdl"),
    config_with("svg", "librsvg"))

def build():
    export("XDG_CONFIG_HOME", build_dir)
    export("XDG_CACHE_HOME", build_dir)
    make()
