metadata = """
summary @ USB Device Utilities
homepage @ http://linux-usb.sourceforge.net/
license @ GPL
src_url @ http://pkgs.fedoraproject.org/repo/pkgs/$name/$fullname.tar.gz/481e1de453bcabbd5f43125bb4df2ab7/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ dev-libs/libusb:1 sys-libs/glibc
"""

usb_ids_date = "2011.08.17"

def prepare():
    rmfile("usb.ids")

    copy("%s/usb.ids-%s" % (filesdir, usb_ids_date), "usb.ids")
    patch(level=1)

def configure():
    raw_configure("--prefix=/usr",
            "--datadir=/usr/share/hwdata",
            "--disable-zlib")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    move("%s/usr/share/pkgconfig" % install_dir, "/usr/lib/pkgconfig")
