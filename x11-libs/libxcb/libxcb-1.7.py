metadata = """
summary @ X11 client-side library
homepage @ http://xcb.freedesktop.org/
license @ MIT
src_url @ http://xcb.freedesktop.org/dist/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc x11-libs/libXdmcp x11-libs/libXau
          x11-proto/xcb-proto

build @ dev-util/pkg-config dev-libs/libxslt dev-lang/python
"""

def prepare():
    patch(level=1)

def configure():
    libtoolize("--force --copy")
    aclocal()
    autoconf()
    automake("--add-missing")
    conf("--enable-xinput")

def build():
    export("PYTHONDONTWRITEBYTECODE", "1")
    make()

def install():
    export("PYTHONDONTWRITEBYTECODE", "1")
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
