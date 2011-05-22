metadata = """
summary @ Library to enable user space application programs to communicate with USB devices
homepage @ http://libusb.sourceforge.net/
license @ LGPL
src_url @ http://downloads.sourceforge.net/libusb/$fullname.tar.bz2
arch @ ~x86
slot @ 1
"""

depends = """
runtime @ sys-libs/glibc
"""

def install():
	raw_install("DESTDIR=%s" % install_dir)

