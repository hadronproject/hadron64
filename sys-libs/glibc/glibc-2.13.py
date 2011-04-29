metadata = """
summary @ GNU C Library
homepage @ http://www.gnu.org/software/libc
license @ GPL-2
src_url @ http://ftp.gnu.org/gnu/$name/$fullname.tar.gz
arch @ ~x86
"""

depends = """
build @ sys-kernel/linux-api-headers
        sys-libs/timezone-data
"""

bdir = "glibc-build"

def prepare():
    patch(level=1)

def configure():
    makedirs("../glibc-build"); cd("../glibc-build")
    echo("slibdir=/lib", "configparms")
    conf("--enable-add-ons=nptl,libidn",
        "--enable-kernel=2.6.27",
        "--with-tls", 
        "--with-__thread",
        "--enable-bind-now", 
        "--without-gd",
        "--without-cvs", 
        "--disable-profile",
        "--disable-multi-arch",
        run_dir = build_dir)

def build():
    makedirs("../glibc-build"); cd("../glibc-build")
    make()

def install():
    makedirs("../glibc-build"); cd("../glibc-build")
    raw_install("install_root=%s install" % install_dir)

    insfile("%s/nscd.conf" % filesdir, "/etc/nscd.conf")
    insexe("%s/locale-gen" % filesdir, "/usr/sbin/locale-gen")
    insexe("%s/nscd" % filesdir, "/etc/rc.d/nscd")
    insfile("%s/nsswitch.conf" % filesdir, "/etc/nsswitch.conf")
    insfile("%s/locale.gen" % filesdir, "/etc/locale.gen")
    #insfile("%s/gai.conf" % filesdir, "/etc/gai.conf")

