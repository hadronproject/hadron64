metadata = """
summary @ ATA S.M.A.R.T. Reading and Parsing Library
homepage @ http://0pointer.de/blog/projects/being-smart.html
license @ LGPL
src_url @ http://0pointer.de/public/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-fs/udev
"""

def configure():
    conf("--disable-static")

def install():
    raw_install("DESTDIR=%s" % install_dir)
