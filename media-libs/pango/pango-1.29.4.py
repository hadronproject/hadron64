metadata = """
summary @ A library for layout and rendering of text
homepage @ http://www.pango.org/
license @ LGPL
src_url @ http://ftp.gnome.org/pub/gnome/sources/pango/1.29/$fullname.tar.bz2
arch @ ~x86
options @ introspection X
"""

depends = """
common @ sys-libs/glib x11-libs/cairo media-libs/freetype media-libs/fontconfig
build @ dev-util/pkg-config media-libs/libpng:1.4
"""

opt_runtime = """
X @ x11-libs/libXrender x11-libs/libX11 >=x11-libs/libXft-2.0.0
"""

opt_build = """
X @ x11-proto/xproto
introspection @ >=dev-libs/gobject-introspection-0.9.5
"""

def configure():
    myopts = ""
    if opt("X"):
        myopts += "  --x-includes=/usr/include --x-libraries=/usr/lib "

    conf(
    config_enable("introspection"),
    config_with("X", "x"),
    "--with-included-modules=basic-fc", myopts)

def build():
    export("HOME", build_dir)
    make()

def install():
    export("HOME", build_dir)
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("AUTHORS", "NEWS", "README", "THANKS")

def post_install():
    system("/sbin/ldconfig -r / &>/dev/null")

    # create pango.modules
    if isfile("/etc/pango/pango.modules"):
        rmfile("/etc/pango/pango.modules")
    system("/usr/bin/pango-querymodules > /etc/pango/pango.modules")
