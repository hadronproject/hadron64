metadata = """
summary @ Keytable files and keyboard utilities
homepage @ ftp://ftp.altlinux.org/pub/people/legion/kbd/
license @ GPL
src_url @ ftp://ftp.altlinux.org/pub/people/legion/$name/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
"""

def prepare():
    patch(level=1)

def configure():
    raw_configure("--prefix=/usr",
            "--datadir=/usr/share/kbd")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("AUTHORS", "ChangeLog", "COPYING", "README")
