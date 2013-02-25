metadata = """
summary @ Implementation of double-array structure for representing trie, as proposed by Junichi Aoe
homepage @ http://linux.thai.net/~thep/datrie/datrie.html
license @ LGPL
src_url @ http://linux.thai.net/pub/thailinux/software/libthai/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
"""

def configure():
    conf("--disable-static")

def install():
    raw_install("DESTDIR=%s" % install_dir)
