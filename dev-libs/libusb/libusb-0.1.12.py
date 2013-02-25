metadata = """
summary @ Library to enable user space application programs to communicate with USB devices
homepage @ http://libusb.sourceforge.net/
license @ LGPL
src_url @ http://downloads.sourceforge.net/libusb/$fullname.tar.gz
arch @ ~x86_64
slot @ 0
"""

depends = """
runtime @ sys-libs/glibc
"""

def configure():
    conf("--disable-debug",
            "--disable-build-docs")

def build():
    make(j=1)

def install():
    raw_install("DESTDIR=%s" % install_dir)
