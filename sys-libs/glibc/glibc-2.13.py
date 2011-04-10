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

secondary_build_dir = "glibc-build"

def prepare():
    patch(level=1)

def configure():
    makedirs(joinpath(install_dir, "etc")); touch(joinpath(install_dir, "etc/ld.so.conf"))
    makedirs(secondary_build_dir); cd(secondary_build_dir)
    system("../configure --prefix=/usr",
    "--mandir=/usr/share/man",
    "--infodir=/usr/share/info",
    "--libexecdir=/usr/lib",
    "--libdir=/usr/lib",
    "--with-headers=/usr/include",
    "--enable-add-ons=nptl,libidn",
    "--enable-kernel=2.6.27",
    "--with-tls",
    "--with-__thread",
    "--enable-bind-now",
    "--without-gd",
    "--without-cvs",
    "--disable-profile",
    "--disable-multi-arch")


def build():
    cd(secondary_build_dir)
    make("CFLAGS='%s -U_FORTIFY_SOURCE'" % get_env("CFLAGS"))

def install():
    cd(secondary_build_dir)
    raw_install("install_root=%s install" % install_dir)



