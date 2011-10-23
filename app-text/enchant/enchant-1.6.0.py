metadata ="""
summary @ Spellchecker wrapping library
homepage @ http://www.abisource.com/enchant/
license @ LGPL-2.1
src_url @ http://www.abisource.com/downloads/$name/$version/$fullname.tar.gz
options @ aspell myspell zemberek
arch @ ~x86
"""

depends = """
build @ sys-libs/glib
"""

opt_build = """
aspell @ virtual/aspell
myspell @ app-text/hunspell
zemberek @ app-text/zemberek
"""

def configure():
    raw_configure("--prefix=/usr",
            "--disable-ispell",
            "--with-myspell-dir=/usr/share/myspell/",
            config_enable("aspell"),
            config_enable("hunspell", "myspell"),
            config_enable("zemberek"))

def install():
    raw_install("DESTDIR=%s install" % install_dir)
    insdoc("AUTHORS", "BUGS", "ChangeLog", "COPYING.LIB", "HACKING",
        "MAINTAINERS", "NEWS", "README", "TODO")
