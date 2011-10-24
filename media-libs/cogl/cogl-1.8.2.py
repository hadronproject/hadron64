metadata = """
summary @ An object oriented GL/GLES Abstraction/Utility Layer
homepage @ http://www.clutter-project.org/
license @ GPL-2
src_url @ http://download.gnome.org/sources/$name/1.8/$fullname.tar.xz
options @ introspection pango
arch @ ~x86
"""

depends = """
common @  >=sys-libs/glib-2.26.0 x11-libs/cairo x11-libs/gdk-pixbuf x11-libs/libdrm
x11-libs/libX11 >=x11-libs/libXcomposite-0.4 x11-libs/libXdamage
x11-libs/libXext >=x11-libs/libXfixes-3 """

opt_common = """
introspection @ >=dev-libs/gobject-introspection-0.9.5
pango @ >=media-libs/pango-1.20.0[introspection] || >=media-libs/pango-1.20.0
"""

build = lambda: (export("HOME", build_dir), make())
install = lambda: (export("HOME", build_dir), raw_install("DESTDIR=%s" % install_dir))

def configure():
    conf("--disable-profile", "--disable-maintainer-flags",
            "--enable-cairo", "--enable-gdk-pixbuf", "--enable-gl",
            "--enable-glx",
            config_enable("introspection"),
            config_enable("pango", "cogl-pango"))
