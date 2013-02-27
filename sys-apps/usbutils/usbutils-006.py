metadata = """
summary @ USB Device Utilities
homepage @ http://www.linux-usb.org/
license @ GPL
src_url @ http://www.kernel.org/pub/linux/utils/usb/$name/$fullname.tar.xz
arch @ ~x86_64
options @ zlib
"""

depends = """
build @ app-arch/xz
runtime @ dev-libs/libusb:1 sys-libs/glibc sys-apps/hwids
"""

opt_runtime = """
zlib @ sys-libs
"""

def prepare():
    patch("level=1")

def configure():
    raw_configure("--prefix=/usr",
            "--datadir=/usr/share/hwdata",
            "--disable-usbids",
            config_enable('zlib'))

def install():
    raw_install("DESTDIR=%s" % install_dir)

    move("%s/usr/share/pkgconfig" % install_dir, "/usr/lib/pkgconfig")
