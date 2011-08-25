metadata = """
summary @ A tool to copy files into or out of a cpio or tar archive
homepage @ http://www.gnu.org/software/cpio
license @ GPL
src_url @ ftp://ftp.gnu.org/gnu/$name/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc
build @ sys-libs/glibc
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)
