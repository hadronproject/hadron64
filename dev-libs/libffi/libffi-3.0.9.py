metadata = """
summary @ A portable, high level programming interface to various calling conventions.
homepage @ http://sourceware.org/libffi
license @ MIT
src_url @ ftp://sourceware.org/pub/libffi/libffi-3.0.9.tar.gz
arch @ ~x86
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("ChangeLog*", "LICENSE", "README*")
