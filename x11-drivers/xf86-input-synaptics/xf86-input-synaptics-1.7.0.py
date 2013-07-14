metadata = """
summary @ Synaptics driver for notebook touchpads
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/driver/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
build @ x11-base/xorg-server x11-libs/libXi x11-libs/libX11 sys-libs/mtdev
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insfile("%s/10-synaptics.conf" % filesdir, "/etc/X11/xorg.conf.d/")
    insdoc("COPYING")
