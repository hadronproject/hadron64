metadata = """
summary @ Freedesktop sound theme 
homepage @ http://freedesktop.org/wiki/Specifications/sound-theme-spec 
license @ GPL-2 + LGPL-2 + CCPL-Attribution-3.0 + CCPL-Attribution-ShareAlike-2.0
src_url @ http://people.freedesktop.org/~mccann/dist/$name-$version.tar.bz2 
arch @ ~x86
"""

depends = """
build @ dev-util/intltool sys-libs/glib sys-devel/gettext
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("AUTHORS", "NEWS", "README")
