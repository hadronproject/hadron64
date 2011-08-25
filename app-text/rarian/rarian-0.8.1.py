metadata = """
summary @ Documentation meta-data library, designed as a replacement for Scrollkeeper
homepage @ http://rarian.freedesktop.org/
license @ GPL
src_url @ http://ftp.gnome.org/pub/gnome/sources/$name/0.8/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ dev-libs/libxslt
"""

def prepare():
    patch(level=0)

def configure():
    conf("--disable-static")

def install():
    raw_install("DESTDIR=%s" % install_dir)
