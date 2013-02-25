metadata = """
summary @  Compiler for the GObject type system
homepage @ http://live.gnome.org/Vala
license @ LGPL-2.1
src_url @ http://download.gnome.org/sources/$name/0.14/$name-$version.tar.bz2
options @ vapigen
slot @ 0.14
arch @ ~x86_64
"""

depends = """
common @ >=sys-libs/glib-2.16
build @ sys-devel/flex dev-util/pkg-config dev-libs/libxslt
"""

def configure():
    conf(config_enable('vapigen'))

def install():
    raw_install('DESTDIR=%s' % install_dir)

    insdoc('ChangeLog', 'NEWS', 'README', 'AUTHORS', 'COPYING')
