metadata = """
summary @ The GNU Compiler Collection
homepage @ http://gcc.gnu.org/
license @ GPL-3
src_url @ ftp://ftp.irisa.fr/pub/mirrors/gcc.gnu.org/gcc/releases/$fullname/$fullname.tar.bz2
arch @ ~x86
"""

def configure():
    makedirs("gcc-build"); cd("gcc-build")
    conf("--enable-shared",
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
    cd("gcc-build")
    make()

def install():
    cd("gcc-build")
    # install gcc
    raw_install("DESTDIR=%s" % install_dir)
    # create symlinks
    makesym("/usr/bin/gcc" , "/usr/bin/cc")
    makesym("/usr/bin/cpp", "/lib/cpp")
