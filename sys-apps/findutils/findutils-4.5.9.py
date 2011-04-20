metadata = """
summary @ GNU utilities for finding files
homepage @ http://www.gnu.org/software/findutils/
license @ GPL-2
src_url @ ftp://alpha.gnu.org/gnu/findutils/findutils-4.5.9.tar.gz
arch @ ~x86
"""

def configure():
    append_cflags('-D_GNU_SOURCE')
    conf()

def install():
    raw_install("DESTDIR=%s install" % install_dir)
