metadata = """
summary @ Command line editor library providing generic line editing, history, and tokenization functions
homepage @ http://www.thrysoee.dk/editline/
license @ BSD
src_url @ http://www.thrysoee.dk/editline/$name-20110227-3.0.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc sys-libs/ncurses
"""

srcdir = fullname+"-3.0"

def configure():
    conf("--enable-widec --enable-static=no")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
