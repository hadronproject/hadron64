metadata = """
summary @ Common C routines used by GTK+ and other libs
homepage @ http://www.gtk.org
license @ LGPL-2
src_url @ http://ftp.gnome.org/pub/GNOME/sources/$name/2.32/$fullname.tar.xz
options @ xattr doc static-libs
arch @ ~x86_64
"""

depends = """
common @ sys-libs/zlib dev-libs/libffi sys-libs/glibc
build @ >=sys-devel/gettext-0.11
"""

opt_common = """
xattr @ sys-apps/attr
"""

def prepare():
    patch("revert-warn-glib-compile-schemas.patch", \
            level=1, reverse=True)

def configure():
    #export("PCRE_LIBS", "-lpcre")
    #export("PCRE_CFLAGS", "-I/usr/include")
    #export("LIBFFI_LIBS", "-lffi")
    #export("LIBFFI_CFLAGS", "-I/usr/lib/libffi-3.0.11/include")
    export("PYTHON", "/usr/bin/python2")
    conf("--with-pcre=system",
            "--with-threads=posix",
            "--disable-fam",
            config_enable("xattr"),
            config_enable("static-libs", "static"))

def install():
    raw_install('DESTDIR=%s' % install_dir)
    makedirs("/etc/profile.d")
    insfile("%s/glib.sh" % filesdir, "/etc/profile.d/glib.sh")
