metadata = """
summary @ A tool to copy files into or out of a cpio or tar archive
homepage @ http://www.gnu.org/software/cpio
license @ GPL
src_url @ ftp://ftp.gnu.org/gnu/$name/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
common @ sys-libs/glibc
"""

def prepare():
    patch("cpio-2.11-non-gnu-compilers.patch")
    patch("cpio-2.11-stat.patch", level=1)
    patch("cpio-2.11-no-gets.patch", level=1)

def install():
    raw_install("DESTDIR=%s" % install_dir)
