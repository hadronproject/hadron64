metadata = """
summary @ A library providing a set of interfaces for accesibility
homepage @ http://www.gtk.org
license @ LGPL
src_url @ http://ftp.acc.umu.se/pub/gnome/sources/$name/2.0/$fullname.tar.bz2
"""

def build():
    export("HOME", build_dir)
    make()

def install():
    export("HOME", build_dir)
    raw_install('DESTDIR=%s' % install_dir)
