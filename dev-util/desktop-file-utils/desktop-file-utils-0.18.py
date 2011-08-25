metadata = """
summary @ Command line utilities for working with desktop entries
homepage @ http://www.freedesktop.org/wiki/Software/desktop-file-utils
license @ GPL
src_url @ http://www.freedesktop.org/software/desktop-file-utils/releases/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glib
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
