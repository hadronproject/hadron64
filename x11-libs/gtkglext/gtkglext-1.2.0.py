metadata = """
summary @ opengl extensions for gtk2
homepage @ http://gtkglext.sourceforge.net/
license @ LGPL
src_url @ http://downloads.sourceforge.net/sourceforge/gtkglext/$name-$version.tar.bz2
arch @ ~x86
"""

depends = """
common @ sys-libs/glib x11-libs/gtk+:2 media-libs/pango[X] media-libs/mesa
build @ dev-util/pkg-config
"""

def prepare():
    system("sed -i 's:-D\(G.*DISABLE_DEPRECATED\):-D__\1__:g' \
            examples/Makefile.am examples/Makefile.in \
            gdk/Makefile.am gdk/Makefile.in \
            gdk/win32/Makefile.am gdk/win32/Makefile.in \
            gdk/x11/Makefile.am gdk/x11/Makefile.in \
            gtk/Makefile.am gtk/Makefile.in"
    )
