metadata = """
summary @ X11 font encoding library
homepage @ http://xorg.freedesktop.org/
license @ MIT
src_url @ http://xorg.freedesktop.org/releases/individual/lib/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc sys-libs/zlib
build @ x11-proto/xproto
"""

def configure():
    conf("--localstatedir=/var --disable-static \
        --with-encodingsdir=/usr/share/fonts/encodings")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
