metadata = """
summary @ List interned atoms defined on server
homepage @ http://xorg.freedesktop.org/
license @ MIT
src_url @ http://xorg.freedesktop.org/archive/individual/app/xlsatoms-$version.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc x11-libs/libxcb
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
