metadata = """
summary @ User-land utilities for LVM2 (device-mapper) software.
homepage @ http://sourceware.org/lvm2/
license @ LGPL2.1
src_url @ ftp://sources.redhat.com/pub/lvm2/LVM2.$version.tgz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc
"""

srcdir = "LVM2.%s" % version

def configure():
    conf("--with-usrlibdir=/usr/lib",
            "--enable-pkgconfig", 
            "--enable-readline", 
            "--enable-dmeventd", 
            "--enable-cmdlib", 
            "--enable-applib",
            "--with-udevdir=/lib/udev/rules.d/", 
            "--enable-udev_sync", 
            "--enable-udev_rules")

def install():
    raw_install("DESTDIR=%s" % install_dir, arg='install_lvm2')
    
    cd("liblvm")
    raw_install("DESTDIR=%s" % install_dir)

    cd("..")
    raw_install("DESTDIR=%s install_device-mapper" % install_dir)

