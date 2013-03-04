metadata = """
summary @ OpenType text shaping engine
homepage @ http://www.freedesktop.org/wiki/Software/HarfBuzz
license @ MIT
src_url @ http://www.freedesktop.org/software/harfbuzz/release/$fullname.tar.bz2
arch @ ~x86_64
options @ static-libs
"""

depends = """
common @ sys-libs/glib dev-libs/icu media-libs/freetype x11-libs/cairo
build @ dev-util/pkg-config
"""

def configure():
   raw_configure(
    "--prefix=/usr/",
    "--exec-prefix=/usr/",
    config_enable("static-libs", "static"))

install = lambda: installd()
