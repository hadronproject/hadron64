metadata = """
summary @ A utility to show the full path of commands
homepage @ http://www.xs4all.nl/~carlo17/which
license @ GPL-3
src_url @ http://www.xs4all.nl/~carlo17/$name/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)
