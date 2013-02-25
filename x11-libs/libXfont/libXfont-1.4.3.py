metadata = """
summary @ X11 font rasterisation library
homepage @ http://xorg.freedesktop.org/
license @ MIT
src_url @ http://xorg.freedesktop.org/archive/individual/lib/libXfont-$version.tar.bz2
arch @ ~x86_64
options @ doc ipv6
"""

depends = """
runtime @ sys-libs/glibc media-libs/freetype x11-libs/libfontenc x11-proto/xproto
          x11-proto/fontsproto x11-libs/xtrans
build @ x11-misc/util-macros x11-libs/xtrans
"""

opt_runtime = """
doc @ app-text/xmlto
"""

def configure():
    conf("--disable-static",
    config_enable("ipv6"),
    config_with("doc", "xmlto"),
    config_enable("doc", "devel-docs"))

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
