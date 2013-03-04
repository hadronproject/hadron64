metadata = """
summary @ X11 client-side library
homepage @ http://xcb.freedesktop.org/
license @ MIT
src_url @ http://xcb.freedesktop.org/dist/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc x11-libs/libXdmcp x11-libs/libXau
          >=x11-proto/xcb-proto-1.7
build @ dev-util/pkg-config dev-libs/libxslt dev-lang/python:2.7
"""

prepare = lambda: patch()

def configure():
    conf("--enable-xinput")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("COPYING")
