metadata = """
summary @ Create an index of scalable font files for X
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/archive/individual/app/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc x11-libs/libfontenc media-libs/freetype
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
