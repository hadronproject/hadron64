metadata = """
summary @ A font management application for the GNOME desktop
homepage @ http://code.google.com/p/font-manager
license @ GPL3
src_url @ http://font-manager.googlecode.com/files/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ dev-lang/python dev-python/pygtk dev-python/pygobject 
          dev-python/pycairo dev-libs/libxml2 media-libs/fontconfig
          media-libs/freetype dev-db/sqlite
build @ dev-lang/python
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("AUTHORS", "ChangeLog", "INSTALL", "NEWS", "README", "TODO")
