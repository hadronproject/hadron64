metadata = """
summary @ Xfce's freedesktop.org specification compatible menu implementation library
homepage @ http://wiki.xfce.org/dev/garcon
license @ LGPL
src_url @ http://archive.xfce.org/src/libs/garcon/0.1/garcon-$version.tar.bz2
arch @ ~x86
options @ debug
"""

depends = """
runtime @ sys-libs/glib
"""

def configure():
    conf("--disable-static",
    config_enable("debug"))

def install():
    raw_install("DESTDIR=%s" % install_dir)
