metadata = """
summary @ The GNU general-purpose parser generator
homepage @ http://www.gnu.org/software/bison/bison.html
license @ GPL-3
src_url @ ftp://ftp.gnu.org/gnu/$name/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc
        sys-devel/m4
"""

def install():
    raw_install("DESTDIR=%s install" % install_dir)
