metadata = """
summary @ Command line tools that assist applications with a variety of desktop integration tasks
homepage @ http://portland.freedesktop.org/
license @ custom
src_url @ http://portland.freedesktop.org/download/$fullname-rc1.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ x11-apps/xset
"""

srcdir = fullname+"-rc1"

def build():
    make("-C scripts")
    make()

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("LICENSE")
