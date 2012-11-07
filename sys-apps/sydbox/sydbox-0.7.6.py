metadata = """
summary @ Pinktrace bases sandboxing tool
homepage @ http://dev.exherbo.org/~alip/pinktrace/
license @ as-is
src_url @ http://dev.exherbo.org/~alip/$name/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
common @ dev-libs/pinktrace[ipv6]
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)
    rmdir("/usr/share/sydbox")
    rmfile("/etc/sydbox.conf")
    insfile("%s/sydbox.conf" % filesdir, "/etc/sydbox.conf")
    insdoc("COPYING", "README.mkd", "AUTHORS.mkd", "NEWS.mkd")
