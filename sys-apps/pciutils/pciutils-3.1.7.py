metadata = """
summary @ PCI bus configuration space access library and tools
homepage @ http://mj.ucw.cz/pciutils.html
license @ GPL-2
src_url @ ftp://ftp.kernel.org/pub/software/utils/$name/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc
build @ net-misc/wget
"""

def build():
    system("./update-pciids.sh")
    make('OPT="%s -fPIC -DPIC" ZLIB=no PREFIX=/usr SHAREDIR=/usr/share/hwdata \
            MANDIR=/usr/share/man all' % get_env('CFLAGS'))

def install():
    raw_install('DESTDIR="%s" \
            SHARED="yes" \
            IDSDIR="/usr/share/misc" \
            MANDIR="/usr/share/man" \
            install-lib' % install_dir)

