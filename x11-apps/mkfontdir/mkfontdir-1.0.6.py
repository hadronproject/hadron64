metadata = """
summary @ Create an index of X font files in a directory
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/archive/individual/app/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc x11-apps/mkfontscale
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
