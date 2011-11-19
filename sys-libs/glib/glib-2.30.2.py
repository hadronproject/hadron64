metadata = """
summary @ Common C routines used by GTK+ and other libs
homepage @ http://www.gtk.org
license @ LGPL-2
src_url @ http://ftp.gnome.org/pub/GNOME/sources/$name/2.30/$fullname.tar.bz2
options @ xattr doc static-libs
"""

depends = """
common @ sys-libs/zlib dev-libs/libffi sys-libs/glibc
build @ >=sys-devel/gettext-0.11
"""

opt_common = """
xattr @ sys-apps/attr
"""

def prepare():
    patch("glib-2.30.2-machine-id.patch", level=1)
    patch("glib-2.30.1-homedir-env.patch", level=1)
    patch("glib-2.30.1-external-gdbus-codegen.patch")
    rmfile("py-compile")
    makesym("/bin/true", "py-compile")

def configure():
    conf("--enable-regex",
            "--with-pcre=system",
            "--with-threads=posix",
            "--disable-fam",
            config_enable("xattr"),
            config_enable("static-libs", "static"))

def install():
    raw_install('DESTDIR=%s' % install_dir)
    makedirs("/etc/profile.d")
    insfile("%s/glib.sh" % filesdir, "/etc/profile.d/glib.sh")
