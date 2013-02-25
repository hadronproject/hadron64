metadata = """
summary @ a C library for manipulating pipelines of subprocesses in a flexible and convenient way
homepage @ http://libpipeline.nongnu.org/
license @ GPL
src_url @ http://download.savannah.gnu.org/releases/libpipeline/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc  dev-util/pkg-config
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)
