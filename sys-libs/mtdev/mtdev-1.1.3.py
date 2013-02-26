metadata = """
summary @ Multitouch Protocol Translation Library
homepage @ http://bitmath.org/code/mtdev/   
license @ MIT
src_url @ http://bitmath.org/code/mtdev/$name-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
build @ sys-kernel/linux-api-headers
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("ChangeLog", "COPYING", "README")
