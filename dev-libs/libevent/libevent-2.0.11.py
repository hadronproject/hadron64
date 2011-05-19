metadata = """
summary @ An event notification library
homepage @ http://www.monkey.org/~provos/libevent/
license @ GPL2
src_url @ http://www.monkey.org/~provos/libevent-$version-stable.tar.gz
arch @ ~x86
"""

depends = """
runtime @ dev-libs/openssl
"""

srcdir = name+"-"+version+"-stable"

print srcdir

def install():
    raw_install("DESTDIR=%s" % install_dir)
