metadata = """
summary @ A library for layout and rendering of text
homepage @ http://www.pango.org/
license @ LGPL
src_url @ http://ftp.gnome.org/pub/gnome/sources/pango/1.32/$fullname.tar.xz
arch @ ~x86_64
options @ introspection X
"""

depends = """
common @ sys-libs/glib x11-libs/cairo media-libs/freetype media-libs/fontconfig media-libs/harfbuzz
build @ dev-util/pkg-config media-libs/libpng
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
            config_with("X", "xft"),
            "--with-included-modules=basic-fc", myopts
    )

def install():
    raw_install("DESTDIR=%s" % install_dir)
    makedirs("/etc/pango")
    insdoc("AUTHORS", "NEWS", "README", "THANKS")

def post_install():
    # create pango.modules
    if isfile("/etc/pango/pango.modules"):
        rmfile("/etc/pango/pango.modules")
    if not system("/usr/bin/pango-querymodules >> /etc/pango/pango.modules"):
        raise BuildError

def post_remove():
    if isfile("/etc/pango/pango.modules"):
        rmfile("/etc/pango/pango.modules")

