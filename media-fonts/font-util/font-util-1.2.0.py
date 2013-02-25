metadata = """
summary @ X.Org font utilities
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/font/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
build @ x11-misc/util-macros
"""

def configure():
    conf(
    "--with-mapdir=/usr/share/fonts/util --with-fontrootdir=/usr/share/fonts")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
