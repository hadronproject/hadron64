metadata = """
summary @ The GIMP Toolkit
homepage @ http://www.gtk.org/
license @ LGPL
src_url @ http://ftp.gnome.org/pub/gnome/sources/gtk+/2.24/$fullname.tar.xz
arch @ ~x86
slot @ 2
options @ xinerama engines introspection
"""

depends = """
common @ x11-libs/libXcursor x11-libs/libXrandr x11-libs/libXi x11-libs/libXcomposite
    x11-libs/libXdamage x11-misc/shared-mime-info x11-libs/cairo[svg]
"""

opt_runtime = """
xinerama @ x11-libs/libXinerama
introspection @ x11-libs/gdk-pixbuf[introspection] media-libs/pango[introspection] dev-libs/atk[introspection]  || x11-libs/gdk-pixbuf media-libs/pango dev-libs/atk
"""

opt_postmerge = """
engines @ x11-themes/gtk-engines
"""

def configure():
    conf(
    "--with-gdktarget=x11",
    "--with-xinput=yes",
    "--enable-xkb",
    "--enable-shm",
    "--enable-silent-rules",
    "--disable-papi",
    config_enable("introspection"),
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
