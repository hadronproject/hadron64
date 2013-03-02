metadata = """
summary @ Library to enable user space application programs to communicate with USB devices
homepage @ http://libusbx.org/
license @ LGPL
src_url @ http://garr.dl.sourceforge.net/project/libusbx/releases/$version/source/$fullname.tar.bz2
arch @ ~x86_64
slot @ 1
"""

depends = """
runtime @ sys-libs/glibc
conflict @ dev-libs/libusb:1
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)
