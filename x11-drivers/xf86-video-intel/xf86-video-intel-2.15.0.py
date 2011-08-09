metadata = """
summary @ X.org evdev input driver
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/driver/$fullname.tar.bz2
arch @ ~x86
options @ dri
"""

depends = """
build @ x11-libs/libXext x11-libs/libXfixes x11-libs/libXvMC >=x11-libs/libxcb-1.5
    x11-base/xorg-server x11-proto/fontsproto x11-proto/xf86driproto
"""

def configure():
    conf(
    config_enable("dri"),
    "--enable-xvmc")

def install():
    raw_install("DESTDIR=%s" % install_dir)

def post_install():
    notify("Warning: This driver requires KMS support in your kernel.")
