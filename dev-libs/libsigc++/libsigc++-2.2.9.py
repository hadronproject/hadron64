metadata = """
summary @ Typesafe callback system for standard C++
homepage @ http://libsigc.sourceforge.net
license @ LGPL2.1
src_url @ http://ftp.gnome.org/pub/GNOME/sources/$name/2.2/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-devel/gcc
build @ sys-devel/gcc
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("AUTHORS", "ChangeLog", "README", "NEWS", "TODO")
