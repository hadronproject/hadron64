metadata = """
summary @ A library providing a set of interfaces for accesibility
homepage @ http://www.gtk.org
license @ LGPL
src_url @ http://ftp.gnome.org/pub/gnome/sources/$name/2.6/$fullname.tar.xz
arch @ ~x86_64
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
    conf(config_enable("introspection"))

def build():
    export("HOME", build_dir)
    make()

def install():
    export("HOME", build_dir)
    raw_install('DESTDIR=%s' % install_dir)
    insdoc("AUTHORS", "ChangeLog", "NEWS", "README")
