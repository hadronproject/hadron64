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
    makedirs(joinpath(install_dir, "etc")); touch(joinpath(install_dir, "etc/ld.so.conf"))
    makedirs("../glibc-build"); cd("../glibc-build")
    conf("--disable-profile",
    "--enable-add-ons",
    "--enable-kernel=2.6.22.5", 
    "--libexecdir=/usr/lib/glibc",
    run_dir = build_dir)

def build():
    makedirs("../glibc-build"); cd("../glibc-build")
    make("CFLAGS='%s -U_FORTIFY_SOURCE'" % get_env("CFLAGS"))

def install():
    makedirs("../glibc-build"); cd("../glibc-build")
    raw_install("install_root=%s install" % install_dir)



