metadata = """
summary @ Hardware Abstraction Layer
homepage @ http://www.freedesktop.org/wiki/Software/hal
license @ GPL-2
src_url @ http://hal.freedesktop.org/releases/$fullname.tar.gz
options @ X acpi apm crypt debug dell disk-partition doc laptop selinux
arch @ ~x86_64
"""

def configure():
    system("libtoolize --force")
    aclocal()
    autoconf()
    automake()
    conf(
        "--libexecdir=/usr/lib/hal",
        "--with-udev-prefix=/etc",
        "--enable-static=no",
        "--disable-console-kit",
        "--disable-policy-kit",
        "--enable-umount-helper",
        "--disable-smbios",
        "--with-hal-user=hal"
        "--with-hal-group=hal",
        "--with-pid-file=/var/run/hald.pid"
        "--disable-gtk-doc")

def install():
    raw_install('DESTDIR=%s' %  install_dir)
