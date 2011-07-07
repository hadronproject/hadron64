metadata = """
summary @ Utilities for monitoring your system and processes on your system
homepage @ http://procps.sourceforge.net/
license @ GPL LGPL
src_url @ http://procps.sourceforge.net/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/ncurses
"""

def prepare():
    patch(level=1)

def install():
    raw_install("DESTDIR=%s ldconfig=/bin/true" % install_dir)
    
    insfile("%s/sysctl.conf" % filesdir, "/etc/sysctl.conf")
    
    insdoc("BUGS", "NEWS", "TODO", "ps/HACKING")
