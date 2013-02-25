metadata = """
summary @ X11 Testing -- Resource extension library
homepage @ http://xorg.freedesktop.org/
license @ MIT
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libXtst-$version.tar.bz2
arch @ ~x86_64
options @ doc
"""

depends = """
runtime @ sys-libs/glibc x11-libs/libXext x11-proto/recordproto x11-proto/inputproto x11-libs/libXi
build @ x11-misc/util-macros
"""

opt_build = """
doc @ app-text/xmlto
"""

def configure():
    conf(
    config_enable("doc", "specs"),
    config_with("doc", "xmlto"),
    "--without-fop",
    "--disable-static")


#srcdir = "libXtst-%s" % version

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
