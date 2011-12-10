metadata = """
summary @ Utility libraries for XC Binding
homepage @ http://xcb.freedesktop.org/
license @ custom
src_url @ http://xcb.freedesktop.org/dist/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc x11-libs/libxcb
build @ dev-util/gperf
"""

def configure():
    conf("--disable-static")

def install():
    raw_install("DESTDIR=%s" % install_dir)
