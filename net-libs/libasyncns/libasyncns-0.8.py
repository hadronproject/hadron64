metadata = """
summary @ A C library for Linux/Unix for executing name service queries asynchronously
homepage @ http://0pointer.de/lennart/projects/libasyncns
license @ LGPL
src_url @ http://0pointer.de/lennart/projects/libasyncns/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc
"""

def prepare():
    patch(level=1)

def configure():
	conf(
	"--disable-dependency-tracking",
	"--disable-lynx",
	"--disable-static")

def install():
	raw_install("DESTDIR=%s" % install_dir)

