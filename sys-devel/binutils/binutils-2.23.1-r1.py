metadata = """
summary @ The GNU Binutils are a collection of binary tools.
homepage @ http://www.gnu.org/software/binutils/
license @ GPL-2
src_url @ http://ftp.gnu.org/gnu/$name/$fullname.tar.bz2
options @ nls
arch @ ~x86_64
"""

depends = """
common @ >=sys-libs/glibc-2.17
runtime @ sys-libs/zlib
"""

def configure():
    makedirs("../binutils-build"); cd("../binutils-build")
    raw_configure(
            "--prefix=/usr",
            "--with-lib-path=/usr/lib:/usr/local/lib",
            "--enable-gold",
            "--enable-threads",
            "--enable-ld=default",
            "--enable-plugins"
            "--enable-shared",
            "--disable-werror",
            # See the following resources about this parameter
            # http://sources.gentoo.org/cgi-bin/viewvc.cgi/gentoo-x86/eclass/toolchain-binutils.eclass?revision=1.122&view=markup
            # http://wiki.osdev.org/GCC_Cross-Compiler_for_x86_64
            #"--enable-64-bit-bfd",
            "--disable-multilib",
            "--with-pic",
        run_dir=build_dir)

def build():
    cd("../binutils-build")
    # checks the host environment and makes sure all the necessary 
    # tools are available
    make("configure-host")

    # build binutils
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
