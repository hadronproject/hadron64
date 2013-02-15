metadata = """
summary @ GNU C Library
homepage @ http://www.gnu.org/software/libc
license @ GPL-2
src_url @ http://ftp.gnu.org/gnu/$name/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
build @ sys-kernel/linux-api-headers
        sys-libs/timezone-data
"""

def prepare():
    patch(location="%s/2.17" % filesdir, level=1)

def configure():
    makedirs("../glibc-build"); cd("../glibc-build")
    echo("slibdir=/lib", "configparms")
    conf("--enable-add-ons=nptl,libidn",
        "--enable-kernel=2.6.32",
        "--enable-obsolete-rpc",
        "--with-tls",
        "--enable-stackguard-randomization",
        "--enable-bind-now",
        "--disable-profile",
        run_dir = build_dir)

def build():
    cd("../glibc-build")
    make()

def install():
    cd("../glibc-build")
    makedirs("/etc")

    raw_install("install_root=%s" % install_dir)

    for item in ('locale', 'systemd/system', 'tmpfiles.d'):
        makedirs("/usr/lib/%s" % item)

    insexe("%s/ld.so.conf" % filesdir, "/etc/ld.so.conf")
    insfile("%s/nscd/nscd.conf" % build_dir, "/etc/nscd.conf")
    insexe("%s/locale-gen" % filesdir, "/usr/bin/locale-gen")
    insfile("%s/nscd.service" % filesdir, "/usr/lib/systemd/system/nscd.service")
    insfile("%s/nscd.tmpfiles" % filesdir, "/usr/lib/tmpfiles.d/nscd.conf")
    insfile("%s/locale.gen" % filesdir, "/etc/locale.gen")
    insfile("%s/locale.gen" % filesdir,  "/etc/locale.gen")
    insfile("%s/posix/gai.conf" % build_dir, "/etc/gai.conf")

    makedirs("/etc/ld.so.conf.d")

    makedirs("/lib64")
    for lib in glob.glob("%s/lib/ld*" % install_dir):
        lib = lib.replace(install_dir, "")
        if not lib.startswith("/"): lib = "/"+lib
        makesym(lib, "/lib64/"+basename(lib))

def post_install():
    warn("Please don't forget to edit /etc/locale.gen and run locale-gen")
