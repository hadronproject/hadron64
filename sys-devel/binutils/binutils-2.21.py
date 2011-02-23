metadata = """
summary @ The GNU Binutils are a collection of binary tools.
homepage @ http://www.gnu.org/software/binutils/
license @ GPL-
src_url @ http://ftp.gnu.org/gnu/$name/$name-$version.tar.gz
options @ nls test
"""

import os

def configure():
    makedirs("binutils-build"); cd("binutils-build")
    export("CC", "/usr/bin/gcc")
    conf("--target='i686-pc-linux-gnu'",
        config_enable("nls"),
        "--with-pkgversion='Hadron'",
        "--disable-werror",
        run_dir=build_dir)

def build():
    cd("binutils-build")
    make("configure-host")
    make("tooldir=%s/usr" % install_dir)
    if opt("test"):
        make("-k check")

def install():
    cd("binutils-build")
    linstall("tooldir=%s/usr" % install_dir)

    for f in ('libiberty.h', 'demangle.h'):
        insfile("%s/include/%s" % (build_dir, f), "/usr/include")

    make("-C libiberty clean")
    make("CFLAGS='%s -fPIC' -C libiberty" % os.environ["CFLAGS"])

    make("-C bfd clean")
    make("CFLAGS='%s -fPIC -fvisibility=hidden' -C bfd" % os.environ["CFLAGS"])
    insfile("bfd/libbfd.a", "/usr/lib")
