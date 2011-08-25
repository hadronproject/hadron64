metadata = """
summary @ GtkSpell provides word-processor-style highlighting and replacement of misspelled words in a GtkTextView widget
homepage @ http://gtkspell.sourceforge.net/
license @ GPL
src_url @ http://gtkspell.sourceforge.net/download/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc dev-util/intltool
"""


def install():
    raw_install("DESTDIR=%s" % install_dir)
