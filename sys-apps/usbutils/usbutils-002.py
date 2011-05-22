metadata = """
summary @ USB Device Utilities
homepage @ http://linux-usb.sourceforge.net/
license @ GPL
src_url @ http://www.kernel.org/pub/linux/utils/usb/$name/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ dev-libs/libusb sys-libs/glibc
"""

def prepare():
    rmfile("usb.ids")

    copy("%s/usb.ids-2011.04.14" % filesdir, "usb.ids")

def configure():
    raw_configure("--prefix=/usr", 
            "--datadir=/usr/share/hwdata", 
            "--disable-zlib")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    move("%s/usr/share/pkgconfig" % install_dir, "/usr/lib/pkgconfig")
