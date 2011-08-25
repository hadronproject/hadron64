metadata = """
summary @ X11 Resource extension library
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libXres-$version.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc x11-libs/libXext
build @ x11-proto/resourceproto x11-proto/damageproto x11-proto/compositeproto
        x11-proto/scrnsaverproto x11-misc/util-macros
"""

#srcdir = "libXres-%s" % version

def configure():
    conf(
    "--disable-static")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
