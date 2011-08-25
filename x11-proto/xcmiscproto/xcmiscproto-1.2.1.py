metadata = """
summary @ X11 XC-Miscellaneous extension wire protocol
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/proto/$fullname.tar.bz2
arch @ ~x86
options @ doc
"""

depends = """
build @ x11-misc/util-macros
"""

opt_build = """
doc @ app-text/xmlto
"""

def configure():
    conf(
    config_enable("doc", "specs"),
    config_with("doc", "xmlto"),
    "--without-fop")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
