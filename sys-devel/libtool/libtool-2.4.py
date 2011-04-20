metadata = """
summary @ A generic library support script
homepage @ http://www.gnu.org/software/libtool
license @ GPL-3
src_url @ ftp://ftp.gnu.org/pub/gnu/$name/$fullname.tar.gz
arch @ ~x86
"""

def install():
    raw_install("DESTDIR=%s install" % install_dir)
