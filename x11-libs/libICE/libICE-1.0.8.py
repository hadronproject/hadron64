metadata = """
summary @ X11 Inter-Client Exchange library
homepage @ http://xorg.freedesktop.org
license @ MIT
src_url @ http://xorg.freedesktop.org/releases/individual/lib/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc x11-proto/xproto
build @ x11-libs/xtrans sys-apps/grep sys-devel/make
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
