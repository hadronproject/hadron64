metadata = """
summary @ Virtual Terminal Emulator widget for use with
homepage @ http://www.gnome.org
license @ LGPL
src_url @ http://ftp.gnome.org/pub/GNOME/sources/vte/0.28/$fullname.tar.bz2
arch @ ~x86
"""

def configure():
    conf("--disable--static",
            "--enable-python")

def build():
    append_cflags("-fno-strict-aliasing")
    make()

def install():
    raw_install("DESTDIR=%s" % install_dir)
