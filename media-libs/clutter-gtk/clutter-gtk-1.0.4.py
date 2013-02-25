metadata = """
summary @ GTK clutter widget
homepage @ http://clutter-project.org/
license @ LGPL
src_url @ http://ftp.acc.umu.se/pub/GNOME/sources/$name/$slot/$fullname.tar.bz2
slot @ 1.0
arch @ ~x86_64
"""

depends = """
common @ >=x11-libs/gtk+-3:3[introspection] media-libs/clutter
dev-libs/gobject-introspection
"""

build = lambda: (export("HOME", build_dir), make())
install = lambda: (export("HOME", build_dir), raw_install("DESTDIR=%s" % install_dir))

def configure():
    conf("--with-flavour=x11", "--enable-maintainer-flags=no",
            "--enable-introspection")
    insdoc("NEWS", "README")
