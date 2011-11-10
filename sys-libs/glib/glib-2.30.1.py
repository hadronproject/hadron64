metadata = """
summary @ Common C routines used by GTK+ and other libs
homepage @ http://www.gtk.org
license @ LGPL-2
src_url @ http://ftp.gnome.org/pub/GNOME/sources/$name/2.30/$fullname.tar.bz2
options @ xattr doc fam selinux static-libs
"""

depends = """
runtime @ dev-libs/pcre
"""

def configure():
    conf(
        "--enable-regex",
        "--with-pcre=system",
        "--with-threads=posix",
        config_enable("doc", "man"),
        config_enable("doc", "gtk-doc"),
        config_enable("fam"),
        config_enable("selinux"),
        config_enable("xattr"),
        config_enable("static-libs", "static"))

def build():
    export("PYTHONDONTWRITEBYTECODE", "1")
    make()

def install():
    export("PYTHONDONTWRITEBYTECODE", "1")
    raw_install('DESTDIR=%s' % install_dir)
