metadata = """
summary @ A library providing a set of interfaces for accesibility
homepage @ http://www.gtk.org
license @ LGPL
src_url @ http://ftp.gnome.org/pub/gnome/sources/$name/1.32/$fullname.tar.bz2
arch @ ~x86_64
"""

def install():
    raw_install('DESTDIR=%s' % install_dir)
