metadata = """
summary @ Linux dynamic and persistent device naming support
homepage @ http://www.kernel.org/pub/linux/utils/kernel/hotplug/udev.html
license @ GPL-2
src_url @ http://www.kernel.org/pub/linux/utils/kernel/hotplug/$fullname.tar.bz2
"""

def prepare():
    patch(level=1)

def configure():
    raw_configure("--prefix=/usr",
        "--sysconfdir=/etc", 
        "--sbindir=/sbin",
        "--with-rootlibdir=/lib", 
        "--libexecdir=/lib/udev",
        "--disable-extras", 
        "--disable-introspection")

def install():
    raw_install('DESTDIR=%s' % install_dir)
    
    insfile("%s/80-drivers.rules" % filesdir, "/lib/udev/rules.d/80-drivers.rules")
    insfile("%s/81-arch.rules" % filesdir, "/lib/udev/rules.d/81-arch.rules")
    insfile("%s/load-modules.sh" % filesdir, "/lib/udev/load-modules.sh")
    insfile("%s/cdsymlinks.sh" % filesdir, "/lib/udev/cdsymlinks.sh")

    for d in ("net", "pts", "shm", "hugepages"):
        makedirs("/lib/udev/devices/%s" % d)

    makesym("/lib/udev/scsi_id", "/sbin/scsi_id")
    
    makedirs("/etc/udev/rules.d")
    
    insdoc("COPYING", "ChangeLog", "README", "TODO", "extras/keymap/README.keymap.txt")

def post_install():
    system("mknod -m 0600 /lib/udev/devices/console c 5 1")
    system("mknod -m 0660 /lib/udev/devices/loop0 b 7 0")
    
    nodes = {"null": "1 3", "zero": "1 5", "kmsg": "1 11", "net/tun": "10 200",
            "fuse": "10 200", "ppp": "108 0"}
    for i in nodes:
        system("mknod -m 0666 /lib/udev/devices/%s c %s" % (i, nodes[i]))


