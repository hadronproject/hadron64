metadata = """
summary @ An image loading library for GTK+ V2
homepage @ http://www.gtk.org/
license @ GPL2
src_url @ http://download.gnome.org/sources/gdk-pixbuf/2.23/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc sys-libs/glib media-libs/libpng media-libs/tiff
          media-libs/jpeg x11-libs/libX11
"""

def configure():
    export("HOME", build_dir)
    conf("--without-libjasper",
            "--with-included-loaders=png")


def build():
    export("HOME", build_dir)
    make()

def install():
    export("HOME", build_dir)
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")

def post_install():
    system("/usr/bin/gdk-pixbuf-query-loaders --update-cache")
