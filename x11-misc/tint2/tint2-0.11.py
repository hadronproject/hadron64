metadata = """
summary @ A basic, good-looking task manager for WMs
homepage @ http://code.google.com/p/tint2/
license @ GPL2
src_url @ http://$name.googlecode.com/files/$name-$version.tar.bz2
arch @ ~x86
"""

depends = """
common @ sys-libs/glib x11-libs/cairo media-libs/pango x11-libs/libX11 x11-libs/libXinerama
    x11-libs/libXdamage x11-libs/libXcomposite x11-libs/libXrender x11-libs/libXrandr media-libs/imlib2
build @ dev-util/cmake dev-util/pkg-config x11-proto/xineramaproto
"""

def prepare():
    patch()

def configure():
    makedirs("build")
    cd("build")
    #myopts = ""
    #if opt("battery"):
    #    myopts += " -DENABLE_BATTERY "
    #else:
    #    myopts += " -DDISABLE_BATTERY "

    #if opt("examples"):
    #    myopts += " -DENABLE_EXAMPLES "
    #else:
    #    myopts += " -DDISABLE_EXAMPLES "

    system("cmake -DCMAKE_INSTALL_PREFIX=/usr ../")
    #FIX add battery examples and this option (cmake-utils_use_enable("tint2conf", "TINT2CONF")

def build():
    pass

def install():
    cd("build")
    raw_install("DESTDIR=%s" % install_dir)

