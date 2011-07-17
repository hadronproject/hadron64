metadata = """
summary @ Shadow password file utilities
homepage @ http://pkg-shadow.alioth.debian.org/
license @ custom
src_url @ http://mir0.gentoo-fr.org/distfiles/$fullname.tar.bz2
arch @ ~x86
"""

def prepare():
    patch(level=1)

def configure():
    system('sed -i "s/noinst_LTLIBRARIES/lib_LTLIBRARIES/g" lib/Makefile.am')
    libtoolize()
    autoreconf()
    append_ldflags("-lcrypt")
    system("sed -i '/^SUBDIRS/s/pam.d//' etc/Makefile.in")

    conf("--enable-shared",
        "--disable-static",
        "--with-libpam",
        "--without-selinux")

def install():
    raw_install("DESTDIR=%s install" % install_dir)

    insfile("%s/adduser" % filesdir, "/usr/sbin/adduser")
    insfile("%s/useradd.defaults" % filesdir, "/etc/default/useradd")
    insfile("%s/login.defs" % filesdir, "/etc/login.defs")

    for i in ('login', 'passwd', 'chgpasswd', 'chpasswd', 'newusers'):
        insfile("%s/%s" % (filesdir, i), "/etc/pam.d/%s" % i)
    insfile("etc/pam.d/groupmems", "/etc/pam.d/groupmems")

    for x in ('chage', 'chfn', 'chsh', 'groupadd', 'groupdel', 'groupmod', 
            'shadow', 'useradd', 'usermod', 'userdel'):
        insfile("%s/defaults.pam" % filesdir, "/etc/pam.d/%s" % x)


