metadata = """
summary @ Common C routines used by GTK+ and other libs
homepage @ http://www.gtk.org
license @ LGPL-2
src_url @ http://ftp.gnome.org/pub/GNOME/sources/$name/2.34/$fullname.tar.xz
options @ xattr doc static-libs
arch @ ~x86_64
"""

depends = """
common @ sys-libs/zlib dev-libs/libffi sys-libs/glibc dev-libs/pcre
build @ >=sys-devel/gettext-0.11 dev-lang/python[xml]:2.7
"""

opt_common = """
xattr @ sys-apps/attr
"""

def prepare():
    patch("revert-warn-glib-compile-schemas.patch", level=1, reverse=True)

def configure():
    conf("--with-pcre=system",
            "--with-threads=posix",
            "--disable-fam",
            config_enable("xattr"),
            config_enable("static-libs", "static"))

def install():
    # TODO: set completiondir
    raw_install('DESTDIR=%s' % install_dir)
