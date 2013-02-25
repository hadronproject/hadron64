metadata = """
summary @ Display information utility for X
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/archive/individual/app/xdpyinfo-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc x11-libs/libX11 x11-libs/libXext x11-libs/libXxf86vm x11-libs/libXxf86dga
          x11-libs/libXrender x11-libs/libXcomposite x11-libs/libXinerama x11-libs/libdmx
          x11-libs/libXtst

build @ x11-misc/util-macros
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
