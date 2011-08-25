metadata = """
summary @ SAX-based renderer for SVG files into a GdkPixbuf
homepage @ http://librsvg.sourceforge.net/
license @ LGPL
src_url @ http://ftp.gnome.org/pub/gnome/sources/$name/2.34/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc x11-libs/gdk-pixbuf media-libs/pango dev-libs/libcroco
build @ dev-util/intltool
"""

def configure():
    conf("--libexecdir=/usr/lib/librsvg \
            --with-croco --disable-static \
            --with-svgz --disable-gtk-theme")

def install():
    raw_install("DESTDIR=%s" % install_dir)
