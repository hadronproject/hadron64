metadata = """
summary @ A GObject based library for creating fast, visually rich graphical user interfaces
homepage @ http://clutter-project.org/
license @ LGPL
src_url @ http://download.gnome.org/sources/$name/1.8/$fullname.tar.xz
arch @ ~x86
"""

depends = """
common @ dev-libs/gobject-introspection x11-libs/libdrm
>=x11-libs/libX11-1.3.1 x11-libs/libXext x11-libs/libXdamage
x11-proto/inputproto >=x11-libs/libXi-1.3 >=x11-libs/libXfixes-3
>=x11-libs/libXcomposite-0.4 media-libs/cogl dev-libs/atk[introspection]
dev-libs/json-glib[introspection] media-libs/pango[introspection]
>=sys-libs/glib-2.28 media-libs/fontconfig"""


build = lambda: (export("HOME", build_dir), make())
install = lambda: (export("HOME", build_dir), raw_install("DESTDIR=%s" % install_dir))

def configure():
    conf("--enable-introspection", "--enable-conformance=no",
            "--disable-gcov", "--enable-profile=no", "--enable-maintainer-flags=no",
            "--enable-xinput", "--with-flavour=glx")

