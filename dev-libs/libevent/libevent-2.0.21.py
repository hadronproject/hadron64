metadata = """
summary @ An event notification library
homepage @ http://www.monkey.org/~provos/libevent/
license @ GPL2
src_url @ https://github.com/downloads/libevent/libevent/libevent-$version-stable.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ dev-libs/openssl
"""

srcdir = name+"-"+version+"-stable"

def install():
    raw_install("DESTDIR=%s" % install_dir)
