metadata = """
summary @ A complete 8086 assembler and loader
homepage @ http://www.debath.co.uk/
license @ GPL-2
src_url @ http://www.debath.co.uk/dev86//$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
common @ sys-libs/glibc
"""

def build():
    make("PREFIX=/usr")

def install():
    makedirs("/usr/bin")
    makedirs("/usr/share/man/man1")
    raw_install("PREFIX=%s/usr MANDIR=%s/usr/share/man/man1" % (install_dir, install_dir))
