metadata = """ 
summary @ Standard GNU file utilities (chmod, cp, dd, dir, ls...), text utilities (sort, tr, head, wc..), and shell utilities (whoami, who,...)
license @ GPL-3
homepage @ http://www.gnu.org/software/coreutils/
src_url @ http://ftp.gnu.org/gnu/coreutils/$fullname.tar.gz
arch @ ~x86
options @ caps gmp xattr nls acl
"""

depends = """
runtime @ sys-libs/glibc dev-libs/pcre
"""

opt_runtime = """
caps @ sys-libs/libcap
gmp @ dev-libs/gmp
acl @ sys-apps/acl
xattr @ sys-apps/attr
nls @ >=sys-devel/gettext-0.15
"""

def prepare():
    # the patches from gentoo linux, our big brother ;)
    patch("8.12", level=1)
    autoreconf("-v")

def configure():
    conf("--with-packager='Hadron'",
            "--with-packager-bug-reports='http://trac.seqizz.net'",
            "--enable-install-program=su",
            "--enable-no-install-program=groups,hostname,kill,uptime",
            "--enable-largefile",
            "--disable-libcap" if not opt("caps") else "",
            config_enable('nls'),
            config_enable('acl'),
            config_enable('xattr'),
            config_with('gmp')
        )

def install():
    raw_install("DESTDIR=%s" % install_dir)
    
    fhs = ('cat', 'chgrp', 'chmod', 'chown', 'cp', 'date', 'dd', 'df', 'echo', 
            'false', 'ln', 'ls', 'mkdir', 'mknod', 'mv', 'pwd', 'rm', 'rmdir', 
            'stty', 'su', 'sync', 'true', 'uname')
    for f in fhs:
        move("%s/usr/bin/%s" % (install_dir, f), "/bin/%s" %  f)

    bins = ('cut', 'dir', 'dircolors', 'du', 'install', 'mkfifo', 'readlink', 
            'shred', 'sleep', 'touch', 'tr', 'vdir')
    for b in bins:
        move("%s/usr/bin/%s" % (install_dir, b), "/bin/%s" %  b)

    makesym("%s/bin/sleep", "/usr/bin/sleep")


