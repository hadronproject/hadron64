metadata = """
summary @ Library providing generic access to the PCI bus and devices
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/lib/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc
build @ x11-misc/util-macros
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("COPYING")
