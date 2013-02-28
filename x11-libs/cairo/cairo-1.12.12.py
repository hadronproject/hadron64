metadata = """
summary @ Cairo vector graphics library
homepage @ http://cairographics.org/
license @ LGPL + MPL
src_url @ http://cairographics.org/releases/$fullname.tar.xz
arch @ ~x86_64
options @ X debug opengl svg xcb drm static-libs
"""

depends = """
common @ media-libs/fontconfig media-libs/freetype media-libs/libpng:1.2 sys-libs/zlib >=x11-libs/pixman-0.18.4 sys-libs/glib 
build @ dev-util/pkg-config sys-devel/libtool app-arch/xz
"""

opt_runtime = """
opengl @ media-libs/mesa
X @ >=x11-libs/libXrender-0.6 x11-libs/libXext x11-libs/libX11 x11-libs/libXft
    drm @ sys-fs/udev
xcb @ x11-libs/libxcb x11-misc/xcb-util
svg @ dev-libs/libxml2
"""

opt_build = """
X @ x11-proto/renderproto
    drm @ x11-proto/xproto >=x11-proto/xextproto-7.1
"""

#TODO: Gallium and some opts

def prepare():
    patch(level=1)

def configure():
    conf(
    config_enable("X", "tee"),
    config_with("X", "x"),
    config_enable("X", "xlib"),
    config_enable("X", "xlib-xrender"),
    config_enable("debug", "test-surfaces"),
    config_enable("opengl", "gl"),
    config_enable("svg"),
    config_enable("xcb"),
    config_enable("xcb", "xcb-shm"),
    config_enable("static-libs", "static"),
    "--enable-ft",
    "--enable-pdf",
    "--enable-png",
    "--enable-ps",
    "--disable-xlib-xcb",
    "--disable-dependency-tracking",
    "--enable-gobject")

def install():
    #debug says parallel install fails
    raw_install("-j1 DESTDIR=%s" % install_dir)
    insdoc("AUTHORS", "ChangeLog", "NEWS", "README")
