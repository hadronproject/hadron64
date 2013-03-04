metadata = """
summary @ X11 Athena Widget library
homepage @ http://xorg.freedesktop.org/
license @ MIT
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libXaw-$version.tar.bz2
arch @ ~x86_64
options @ doc
"""

depends = """
runtime @ sys-libs/glibc x11-libs/libXmu x11-libs/libXpm
build @ x11-misc/util-macros
"""

opt_runtime = """
doc @ app-text/xmlto
"""

def configure():
    conf(
    "--disable-static",
    config_enable("doc", "specs"),
    config_with("doc", "xmlto"))

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("COPYING")
