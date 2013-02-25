metadata = """
summary @ X11 Record extension wire protocol
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/proto/$fullname.tar.bz2
arch @ ~x86_64
options @ doc
"""

depends = """
runtime @ x11-misc/util-macros
"""

opt_build = """
doc @ app-text/xmlto
"""

def configure():
    export("HOME", build_dir)
    conf(
    config_enable("doc", "specs"),
    config_with("doc", "xmlto"),
    "--without-fop")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
