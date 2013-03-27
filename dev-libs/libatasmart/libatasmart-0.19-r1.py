metadata = """
summary @ ATA S.M.A.R.T. Reading and Parsing Library
homepage @ http://0pointer.de/blog/projects/being-smart.html
license @ LGPL
src_url @ http://0pointer.de/public/$fullname.tar.xz
arch @ ~x86_64
"""

depends = """
runtime @ sys-apps/systemd
"""

def configure():
    conf("--disable-static")

def install():
    raw_install("DESTDIR=%s" % install_dir)
