metadata = """
summary @ An 80x86 assembler designed for portability and modularity
homepage @ http://www.nasm.us/
license @ BSD
src_url @ http://www.nasm.us/pub/nasm/releasebuilds/$version/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
"""

def install():
    raw_install("INSTALLROOT=%s" % install_dir)

