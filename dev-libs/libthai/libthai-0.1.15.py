metadata = """
summary @ Thai language support routines
homepage @ http://linux.thai.net/projects/libthai
license @ LGPL
src_url @ http://linux.thai.net/pub/thailinux/software/libthai/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ dev-libs/libdatrie
"""

def configure():
    conf("--disable-static")

def install():
    raw_install("DESTDIR=%s" % install_dir)
