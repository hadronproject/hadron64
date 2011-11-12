metadata = """
summary @ The GNU Compiler Collection
homepage @ http://gcc.gnu.org/
license @ GPL-3 LGPL-3
src_url @ ftp://gcc.gnu.org/pub/gcc/snapshots/4.6-20110408/gcc-4.6-20110408.tar.bz2
arch @ ~x86
"""

depends = """
common @ sys-devel/binutils dev-libs/mpc sys-apps/sed >=sys-libs/zlib-1.1.4 
>=dev-libs/mpfr-2.4.2
build @ >=sys-apps/texinfo-4.8 >=sys-devel/bison-1.875 >=sys-devel/flex-2.5.4
"""

srcdir = name+"-4.6-20110408"

def configure():
    system("sed -i 's/install_to_$(INSTALL_DEST) //' libiberty/Makefile.in")
    system("sed -i 's@\./fixinc\.sh@-c true@' gcc/Makefile.in")

    makedirs("../gcc-build"); cd("../gcc-build")
    conf("--enable-shared",
        "--enable-gold",
        "--enable-threads=posix",
        "--enable-__cxa_atexit",
        "--enable-clocale=gnu",
        "--enable-languages=c,c++",
        "--disable-multilib",
        "--disable-bootstrap",
        "--with-system-zlib",
        "--with-pkgversion='Hadron'",
        "--with-bugurl=http://bugzilla.hadronproject.org",
        run_dir=build_dir)

def build():
    cd("../gcc-build")
    make()

def install():
    cd("../gcc-build")
    # install gcc
    raw_install("DESTDIR=%s" % install_dir)
    # create symlinks
    makesym("/usr/bin/gcc" , "/usr/bin/cc")
    makesym("/usr/bin/cpp", "/lib/cpp")
