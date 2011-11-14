metadata = """
summary @ GNU C Library
homepage @ http://www.gnu.org/software/libc
license @ GPL-2
src_url @ http://ftp.gnu.org/gnu/$name/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
build @ sys-kernel/linux-api-headers
        sys-libs/timezone-data
"""

def prepare():
    patch(location="%s/2.14" % filesdir, level=1)

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
    cd("../glibc-build")
    make()

def install():
    cd("../glibc-build")
    makedirs("/etc")
    touch("/etc/ld.so.conf")
    raw_install("install_root=%s" % install_dir)

    rmfile("/etc/ld.so.conf")

    makedirs("/usr/lib/locale")
    
    insfile("%s/nscd.conf" % filesdir, "/etc/nscd.conf")
    insexe("%s/locale-gen" % filesdir, "/usr/sbin/locale-gen")
    insexe("%s/nscd" % filesdir, "/etc/rc.d/nscd")
    insfile("%s/nsswitch.conf" % filesdir, "/etc/nsswitch.conf")
    insfile("%s/locale.gen" % filesdir, "/etc/locale.gen")
    insfile("%s/locale.gen" % filesdir,  "/etc/locale.gen")
    #FIXME: #insfile("%s/glibc/posix/gai.conf" % build_dir, "/etc/gai.conf")
    
    makedirs("/etc/ld.so.conf.d")

def post_install():
    warn("Please don't forget to edit /etc/locale.gen and run locale-gen")
