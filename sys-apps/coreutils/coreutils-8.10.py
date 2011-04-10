metadata = """ 
summary @ Standard GNU file utilities (chmod, cp, dd, dir, ls...), text utilities (sort, tr, head, wc..), and shell utilities (whoami, who,...)
license @ GPL-3
homepage @ http://www.gnu.org/software/coreutils/
src_url @ http://ftp.gnu.org/gnu/coreutils/coreutils-8.10.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc sys-libs/pam 
        sys-apps/acl dev-libs/gmp 
        sys-apps/shadow
"""

def configure():
    autoreconf("-v")
    conf("--enable-install-program=su",
         "--enable-no-install-program=groups,hostname,kill,uptime"
         )

def install():
    raw_install("DESTDIR=%s" % install_dir)
