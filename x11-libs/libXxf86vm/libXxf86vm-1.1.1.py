metadata = """
summary @ X11 XFree86 video mode extension library
homepage @ http://xorg.freedesktop.org/
license @ MIT
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libXxf86vm-$version.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc x11-libs/libXext x11-proto/xf86vidmodeproto
build @ x11-misc/util-macros
"""

#srcdir = "libXxf86vm-%s" % version

def configure():
    conf(
    "--disable-static")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
