metadata = """
summary @ A portable, high level programming interface to various calling conventions.
homepage @ http://sourceware.org/libffi
license @ MIT
src_url @ ftp://sourceware.org/pub/$name/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
common @ sys-libs/glibc
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("ChangeLog*", "LICENSE", "README*")
