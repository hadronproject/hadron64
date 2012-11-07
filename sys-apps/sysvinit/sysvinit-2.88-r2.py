metadata = """
summary @ System V Init
homepage @ http://savannah.nongnu.org/projects/sysvinit
license @ GPL
src_url @ http://download.savannah.gnu.org/releases/sysvinit/$fullnamedsf.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-apps/gawk sys-apps/shadow sys-apps/util-linux 
sys-apps/coreutils sys-libs/glibc
"""

srcdir = name+"-2.88dsf"

def prepare():
    sed("-i 's@Sending processes@& configured via /etc/inittab@g' \
            src/init.c")
    sed("-i -e 's/utmpdump wall/utmpdump/' \
            -e '/= mountpoint/d' \
            -e 's/mountpoint.1 wall.1//' src/Makefile")

build = lambda: make("-C src")
install = lambda: raw_install("-C src ROOT=%s" % install_dir)

