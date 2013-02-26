blame = """
alias @ purak
packager @ Burak Sezer <purak{et}hadronproject.org>
bugs_to @ toolchain{et}hadronproject.org
"""

metadata = """
summary @ System and service manager for Linux
homepage @ http://www.freedesktop.org/wiki/Software/systemd
license @ GPL-2 LGPL-2.1 MIT
src_url @ http://www.freedesktop.org/software/systemd/$fullname.tar.xz
arch @ ~x86_64
"""

depends = """
runtime @ sys-apps/hwids
build @ dev-perl/XML-Parser dev-util/gperf dev-libs/gobject-introspection
common @ >=sys-apps/util-linux-2.20 >=sys-apps/dbus-1.6.8 sys-libs/libcap
sys-apps/acl >=sys-apps/kmod-12 sys-libs/pam sys-apps/attr
"""

# TODO:
# * We must use various option to control this package. Here's a little list :)
# * IUSE="acl audit cryptsetup gcrypt http +kmod lzma pam python qrcode selinux tcpd vanilla xattr"
# * We must create a proper post_install function to complete installation

def prepare():
    sed("-i -e '1s/python/&2.7/' src/analyze/systemd-analyze")

def configure():
    raw_configure("--localstatedir=/var",
            "--with-rootprefix=/usr",
            "--with-rootlibdir=/usr/lib",
            "--with-pamlibdir=/usr/lib/security",
            "--enable-split-usr",
            "--disable-gtk-doc",
            "--enable-gudev",
            "--enable-introspection",
            "--enable-acl",
            "--enable-kmod",
            "--enable-pam",
            "--enable-xattr",
            "--disable-audit",
            "--disable-ima",
            "--with-sysvinit-path=",
            "--with-sysvrcnd-path=")

def install():
    installd()
    echo("d /run/console 0755 root root\n", "/usr/lib/tmpfiles.d/console.conf")
    sed("""-i 's#GROUP="dialout"#GROUP="uucp"#g;
                s#GROUP="tape"#GROUP="storage"#g;
                s#GROUP="cdrom"#GROUP="optical"#g' %s/usr/lib/udev/rules.d/*.rules""" % install_dir)
    makesym("../lib/systemd/systemd-udevd", "/usr/bin/udevd")
    makesym("../usr/bin/udevadm", "/sbin/udevadm")
    makesym("../usr/lib/systemd/systemd", "/bin/systemd")
    makedirs("/var/log/journal")

