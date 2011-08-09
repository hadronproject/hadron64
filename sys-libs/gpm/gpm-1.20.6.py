metadata = """
summary @ A mouse server for the console and xterm
homepage @ http://www.nico.schottelius.org/software/gpm/
license @ GPL
src_url @ http://www.nico.schottelius.org/software/gpm/archives/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/ncurses app-shells/bash
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("BUGS", "Changes", "README", "TODO")
