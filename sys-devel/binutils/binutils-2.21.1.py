metadata = """
summary @ The GNU Binutils are a collection of binary tools.
homepage @ http://www.gnu.org/software/binutils/
license @ GPL-2
src_url @ ftp://ftp.archlinux.org/other/binutils/$fullname_20110627.tar.bz2
options @ nls
arch @ ~x86
"""

depends = """
common @ sys-libs/glibc
runtime @ sys-libs/zlib
build @ sys-devel/flex
"""

srcdir = "binutils"

def configure():
    makedirs("../binutils-build"); cd("../binutils-build")
    conf("--enable-gold",
        "--enable-threads",
        "--enable-ld=default",
        "--enable-plugins"
        "--enable-shared",
        "--disable-werror",
        run_dir=build_dir)

def build():
    cd("../binutils-build")
    make("configure-host")
    make("tooldir=%s/usr" % install_dir)

def install():
    cd("../binutils-build")
    linstall("tooldir=%s/usr install" %  install_dir)

    for f in ('libiberty.h', 'demangle.h'):
        insfile("%s/include/%s" % (build_dir, f), "/usr/include")

    make("-C libiberty clean")
    make("CFLAGS='%s -fPIC' -C libiberty" % get_env("CFLAGS"))

    make("-C bfd clean")
    make("CFLAGS='%s -fPIC -fvisibility=hidden' -C bfd" % get_env("CFLAGS"))
    insfile("bfd/libbfd.a", "/usr/lib")

    for lib in ('libbfd', 'libopcodes'):
        if isexists("%s/usr/lib/%s.so" % (install_dir, lib)):
            rmfile("/usr/lib/%s.so" % lib)

    echo("INPUT ( /usr/lib/libbfd.a -liberty -lz )", "/usr/lib/libbfd.so")
    echo("INPUT ( /usr/lib/libopcodes.a -lbfd )", "/usr/lib/libopcodes.so")
