metadata = """
summary @ Disk Management Service
homepage @ http://www.freedesktop.org/wiki/Software/udisks
license @ GPL
src_url @ http://hal.freedesktop.org/releases/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime  @ sys-apps/systemd sys-apps/sg3_utils sys-libs/glib dev-libs/dbus-glib
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
    raw_install("profiledir=/usr/share/bash-completion/completions DESTDIR=%s" % install_dir)
    setmod("644 %s/usr/share/bash-completion/completions/udisks-bash-completion.sh" % install_dir)
    move("/lib/udev", "/usr/lib/")
    rmdir("/lib")

    insfile("%s/udisks.service" % filesdir, "/usr/lib/systemd/system/udisks.service")
    echo("SystemdService=udisks.service", "/usr/share/dbus-1/system-services/org.freedesktop.UDisks.service")

