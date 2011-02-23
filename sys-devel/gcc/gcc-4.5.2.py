metadata = """
summary @ The GNU Compiler Collection
homepage @ http://gcc.gnu.org/
license @ GPL-3
src_url @ ftp://ftp.irisa.fr/pub/mirrors/gcc.gnu.org/gcc/releases/gcc-4.5.2/gcc-4.5.2.tar.bz2
options @ fortran gtk mudflap nls openmp
"""

def configure():
    makedirs("gcc-build"); cd("gcc-build")
    conf("--target='%s'" % get_env("HOST"),
        "--disable-nsl",
        "--disable-shared",
        "--disable-multilib",
        "--disable-decimal-float",
        "--disable-threads"
        "--disable-libmudflap",
        "--disable-libssp"
        "--disable-libgomp",
        "--enable-languages=c",
        "--with-gmp-include=%s/gmp" % pwd(),
        "--with-gmp-lib=%s/gmp/.libs" % pwd(),
        "--without-ppl --without-cloog",
        "--with-pkgversion='Hadron'",
        "--with-bugurl=http://bugzilla.hadronproject.org",
        run_dir=build_dir)

def build():
    cd("gcc-build")
    make()

def install():
    cd("gcc-build")
    raw_install("DESTDIR=%s" % install_dir)
