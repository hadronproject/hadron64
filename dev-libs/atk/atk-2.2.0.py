metadata = """
summary @ A library providing a set of interfaces for accesibility
homepage @ http://www.gtk.org
license @ LGPL
src_url @ http://ftp.acc.umu.se/pub/gnome/sources/$name/2.2/$fullname.tar.bz2
options @ introspection nls 
"""

depends = """
common @ sys-libs/glib
build @ dev-lang/perl dev-util/pkg-config
"""

opt_runtime = """
introspection @ dev-libs/gobject-introspection 
"""

opt_build = """
nls @ sys-devel/gettext
"""

def configure():
    system("sed -e '/-D[A-Z_]*DISABLE_DEPRECATED/d' -i atk/Makefile.am atk/Makefile.in tests/Makefile.am tests/Makefile.in")
    conf(config_enable("introspection"))

def build():
    export("HOME", build_dir)
    make()

def install():
    export("HOME", build_dir)
    raw_install('DESTDIR=%s' % install_dir)
    insdoc("AUTHORS", "ChangeLog", "NEWS", "README")
