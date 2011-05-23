metadata = """
summary @ Disk Management Service
homepage @ http://www.freedesktop.org/wiki/Software/udisks
license @ GPL
src_url @ http://hal.freedesktop.org/releases/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime  @ sys-fs/udev sys-apps/sg3_utils sys-libs/glib dev-libs/dbus-glib
           sys-auth/polkit sys-block/parted dev-libs/libatasmart sys-process/lsof
           sys-fs/lvm sys-block/eject
build @ dev-util/intltool
"""

def prepare():
    patch(level=1)

def configure():
    raw_configure("--prefix=/usr", 
            "--sysconfdir=/etc", 
            "--localstatedir=/var",
            "--libexecdir=/usr/lib/udisks", 
            "--disable-static",
            "--disable-gtk-doc",
            "--disable-man-pages")

def install():
    raw_install("DESTDIR=%s" % install_dir)

