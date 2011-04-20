metadata = """
summary @  Compiler for the GObject type system
homepage @ http://live.gnome.org/Vala
license @ LGPL-2.1
src_url @ http://download.gnome.org/sources/$name/0.11/$name-$version.tar.bz2
options @ vapigen
"""

def configure():
    conf(config_enable('vapigen'))

def install():
    raw_install('DESTDIR=%s' % install_dir)

    insdoc('NEWS', 'README', 'AUTHORS', 'COPYING')
