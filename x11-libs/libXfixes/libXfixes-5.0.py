metadata = """
summary @ X11 miscellaneous 'fixes' extension library
homepage @ http://xorg.freedesktop.org/
license @ MIT
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libXfixes-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc x11-proto/fixesproto x11-libs/libX11
build @ x11-misc/util-macros
"""

#srcdir = "libXfixes-%s" % version

def configure():
    conf(" --disable-static")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
