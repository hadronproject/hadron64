metadata = """
summary @ ORBit2 is a high-performance CORBA ORB
homepage @ http://www.gnome.org/
license @ LGPL GPL
src_url @ http://ftp.gnome.org/pub/gnome/sources/ORBit2/2.14/ORBit2-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ dev-libs/libidl
"""

srcdir = "ORBit2-%s" % version

def configure():
    conf("--disable-static")

def install():
    raw_install("DESTDIR=%s" % install_dir)
