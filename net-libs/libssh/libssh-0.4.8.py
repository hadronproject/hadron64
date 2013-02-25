metadata = """
summary @ Library for accessing ssh client services through C libraries
homepage @ http://www.libssh.org/
license @ LGPL
src_url @ http://www.libssh.org/files/0.4/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ dev-libs/openssl
build @ dev-util/cmake
"""

def build():
    makedirs("../build")
    cd("../build")
    # FIXME: cmake_utils will be prepared.
    system("cmake ../%s \
            -DCMAKE_INSTALL_PREFIX=/usr \
            -DCMAKE_BUILD_TYPE=Release" % fullname)
    make()

def install():
    cd("../build")
    raw_install("DESTDIR=%s" % install_dir)

    #insdoc("COPYING")
