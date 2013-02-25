metadata = """
summary @ GTK+ implementation of wxWidgets API for GUI
homepage @ http://wxwidgets.org
license @ wxWinLL-3 GPL-2
src_url @ http://downloads.sourceforge.net/wxpython/wxPython-src-$version.tar.bz2
arch @ ~x86_64
options @ X debug gstreamer odbc opengl sdl tiff pch
"""

#TODO: More options http://znurt.org/x11-libs/wxGTK/wxGTK-2.8.12.0

depends = """
runtime @ dev-libs/expat
build @ dev-util/pkg-config
"""

opt_runtime = """
X @ >=x11-libs/gtk+-2.4:2 >=sys-libs/glib-2.4 media-libs/jpeg x11-libs/libSM x11-libs/libXinerama x11-libs/libXxf86vm
    gstreamer @ gnome-base/gconf >=media-libs/gstreamer-0.10 >=media-libs/gst-plugins-base-0.10
    opengl @ media-libs/mesa
    tiff @ media-libs/tiff
sdl @ media-libs/SDL
odbc @ dev-db/unixODBC
"""

opt_build = """
X @ x11-proto/xproto x11-proto/xineramaproto x11-proto/xf86vidmodeproto
"""

srcdir = "wxPython-src-" + version

def prepare():
    patch(level=1)

def configure():
    myconf = " --enable-compat26 --enable-shared --enable-unicode \
            --with-regex=builtin --with-zlib=sys --with-expat=sys "
    
    if opt("X"):
        myconf += "--enable-graphics_ctx \
                --enable-gui \
                --with-libpng=sys \
                --with-libxpm=sys \
                --with-libjpeg=sys \
                --without-gnomevfs "
        if opt("gstreamer"):
            myconf += " --enable-mediactrl "
        else:
            myconf += " --disable-mediactrl "
        if opt("opengl"):
            myconf += " --enable-opengl --with-opengl "
        else:
            myconf += " --disable-opengl --without-opengl "
    else:
        myconf += " --disable-gui "

    conf(
        config_enable("debug"),
        config_enable("pch", "precomp-headers"),
        config_with("odbc", "odbc=sys"),
        config_with("sdl"),
        config_with("tiff", "libtiff=sys"), myconf)

def build():
    make()
    make("-C locale allmo")
    cd("contrib/src")
    make()

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("changes.txt", "readme.txt", "todo30.txt", "base/readme.txt",
            "base_readme.txt", "gtk/readme.txt", "gtk_readme.txt")
    cd("contrib/src")
    raw_install("DESTDIR=%s" % install_dir)
