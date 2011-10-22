metadata = """
summary @ A Free Implementation of the Unicode Bidirectional Algorithm
homepage @ http://fribidi.org/
license @ LGPL
src_url @ http://fribidi.org/download/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc
"""

def build():
    conf("--prefix=/usr")
    
def install():
    raw_install("DESTDIR=%s" % install_dir) 
