metadata = """
summary @ Standard GNU file utilities (chmod, cp, dd, dir, ls...), text utilities (sort, tr, head, wc..), and shell utilities (whoami, who,...)
license @ GPL-3
homepage @ http://www.gnu.org/software/coreutils/
src_url @ http://ftp.gnu.org/gnu/coreutils/$fullname.tar.xz
arch @ ~x86
options @ caps gmp xattr nls acl pam
"""

depends = """
common @ sys-libs/glibc dev-libs/pcre sys-apps/shadow
"""

opt_runtime = """
caps @ sys-libs/libcap
gmp @ dev-libs/gmp
acl @ sys-apps/acl
xattr @ sys-apps/attr
nls @ >=sys-devel/gettext-0.15
pam @ sys-libs/pam
"""

def prepare():
    # the patches from lfs
    patch("8.14", level=1)

def configure():
    conf("--with-packager='Hadron Project'",
            "--with-packager-bug-reports='http://trac.seqizz.net'",
            "--enable-install-program=su",
            "--enable-no-install-program=groups,hostname,kill,uptime",
            "--enable-largefile",
            "--disable-libcap" if not opt("caps") else "",
            config_enable('nls'),
            config_enable('acl'),
            config_enable('xattr'),
            config_with('gmp'),
            config_enable('pam')
        )

def install():
    raw_install("DESTDIR=%s" % install_dir)

    fhs = ('cat', 'chgrp', 'chmod', 'chown', 'cp', 'date', 'dd', 'df', 'echo',
            'false', 'ln', 'ls', 'mkdir', 'mknod', 'mv', 'pwd', 'rm', 'rmdir',
            'stty', 'su', 'sync', 'true', 'uname')
    for f in fhs:
        move("/usr/bin/%s" %  f, "/bin/%s" %  f)

    bins = ('cut', 'dir', 'dircolors', 'du', 'install', 'mkfifo', 'readlink',
            'shred', 'sleep', 'touch', 'tr', 'vdir')
    for b in bins:
        move("/usr/bin/%s" % b, "/bin/%s" %  b)

    makesym("/bin/sleep", "/usr/bin/sleep")
