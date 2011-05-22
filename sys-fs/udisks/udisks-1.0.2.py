metadata = """
summary @ Disk Management Service
homepage @ http://www.freedesktop.org/wiki/Software/udisks
license @ GPL
src_url @ http://hal.freedesktop.org/releases/$fullname.tar.gz
arch @ ~x86
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

