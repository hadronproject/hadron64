metadata = """
summary @ A library providing a set of interfaces for accesibility
homepage @ http://www.gtk.org
license @ LGPL
src_url @ http://ftp.acc.umu.se/pub/gnome/sources/$name/2.0/$fullname.tar.bz2
"""

def install():
    raw_install('DESTDIR=%s' % install_dir)
