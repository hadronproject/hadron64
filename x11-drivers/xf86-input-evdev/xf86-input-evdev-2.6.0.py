metadata = """
summary @ X.org evdev input driver
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/driver/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
build @ x11-base/xorg-server
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insfile("%s/10-evdev.conf" % filesdir, "/etc/X11/xorg.conf.d/10-evdev.conf")

    insdoc("COPYING")
