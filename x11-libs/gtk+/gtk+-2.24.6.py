metadata = """
summary @ The GIMP Toolkit
homepage @ http://www.gtk.org/
license @ LGPL
src_url @ http://ftp.gnome.org/pub/gnome/sources/gtk+/2.24/$fullname.tar.bz2
arch @ ~x86
slot @ 2
options @ xinerama
"""

depends = """
build @ dev-libs/atk media-libs/pango x11-libs/libXcursor x11-libs/libXrandr
        x11-libs/libXi x11-libs/libXcomposite x11-libs/libXdamage x11-misc/shared-mime-info x11-libs/cairo
        x11-libs/gdk-pixbuf

runtime @ dev-libs/atk media-libs/pango x11-libs/libXcursor x11-libs/libXrandr
          x11-libs/libXi x11-libs/libXcomposite x11-libs/libXdamage x11-misc/shared-mime-info x11-libs/cairo
          x11-libs/gdk-pixbuf
"""

opt_runtime = """
xinerama @ x11-libs/libXinerama
"""

def prepare():
    patch(level=1)
    patch("gtk2-dont-ellipsize-filters.diff", level=1)

def configure():
    conf("--with-gdktarget=x11 \
            --with-xinput=yes \
            --enable-xkb \
            --enable-shm \
            --enable-silent-rules \
            --disable-papi",
            config_enable("xinerama"))
    #system("sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool")

def build():
    export("HOME", build_dir)
    make()

def install():
    export("HOME", build_dir)
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("AUTHORS", "README*", "HACKING", "ChangeLog*", "NEWS*")

def post_install():
    system("/usr/bin/gtk-query-immodules-2.0 > /etc/gtk-2.0/gtk.immodules")
