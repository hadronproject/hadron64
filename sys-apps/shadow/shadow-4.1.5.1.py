metadata = """
summary @ Shadow password file utilities
homepage @ http://pkg-shadow.alioth.debian.org/
license @ custom
src_url @ http://pkg-shadow.alioth.debian.org/releases/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-apps/acl app-shells/bash sys-libs/pam
"""

def prepare():
    sed("-i '/^user\(mod\|add\)_LDADD/s|$| -lattr|' src/Makefile.am")
    patch(level=1)
    sed("-i '/^SUBDIRS/s/pam.d//' etc/Makefile.in")

def configure():
    libtoolize()
    #autoreconf()
    append_ldflags("-lcrypt")

    conf("--enable-shared",
        "--disable-static",
        "--with-libpam",
        "--without-selinux")

def install():
    raw_install("DESTDIR=%s install" % install_dir)

    insexe("%s/adduser" % filesdir, "/usr/sbin/adduser")
    insfile("%s/useradd.defaults" % filesdir, "/etc/default/useradd")
    insfile("%s/login.defs" % filesdir, "/etc/login.defs")

    for i in ('login', 'passwd', 'chgpasswd', 'chpasswd', 'newusers'):
        insfile("%s/%s" % (filesdir, i), "/etc/pam.d/%s" % i)
    insfile("etc/pam.d/groupmems", "/etc/pam.d/groupmems")

    for x in ('chage', 'chfn', 'chsh', 'groupadd', 'groupdel', 'groupmod',
            'shadow', 'useradd', 'usermod', 'userdel'):
        insfile("%s/defaults.pam" % filesdir, "/etc/pam.d/%s" % x)

    # these files are shipped by coreutils
    rmfile("/bin/su")
    rmfile("/usr/share/man/man1/su.1")
