metadata = """
summary @ System V Init
homepage @ http://savannah.nongnu.org/projects/sysvinit
license @ GPL
src_url @ http://download.savannah.gnu.org/releases/sysvinit/$fullnamedsf.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-apps/shadow sys-apps/util-linux sys-apps/coreutils sys-libs/glibc
"""
srcdir = fullname+"dsf"

def install():
    raw_install("ROOT=%s" % install_dir)
