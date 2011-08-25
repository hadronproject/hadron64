metadata = """
summary @ X.Org authorization settings program
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/archive/individual/app/xauth-$version.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc x11-libs/libXmu
"""

#srcdir = "xauth-%s" % version

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
