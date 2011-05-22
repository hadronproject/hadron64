metadata = """
summary @ An HTTP library implementation in C
homepage @ http://live.gnome.org/LibSoup
license @ LGPL-2
src_url @ http://ftp.gnome.org/pub/gnome/sources/libsoup/2.34/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ dev-util/libxml2 sys-libs/glib
"""

def configure():
    conf("--disable-static",
            "--disable-tls-check")

# FIXME: tls desteginin acilmasi gerek

def build():
    export("HOME", build_dir)
    make()

def install():
    raw_install("DESTDIR=%s" % install_dir)

