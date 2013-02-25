metadata = """
summary @ Spell checker and morphological analyzer library and program
homepage @ http://hunspell.sourceforge.net/
license @ GPL LGPL MPL
src_url @ http://downloads.sourceforge.net/hunspell/$fullname.tar.gz
options @ ncurses nls readline static-libs
arch @ ~x86_64
"""

depends = """
common @ sys-devel/gettext
"""

opt_common = """
ncurses @ sys-libs/ncurses
readline @ sys-libs/readline
"""


def configure():
    conf(config_enable("static-libs", "static"),
            config_with("readline"),
            config_with("ncurses", "ui"),
            config_enable("nls"))

def install():
    raw_install("DESTDIR=%s" % install_dir)

