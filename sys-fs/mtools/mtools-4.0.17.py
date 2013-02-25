metadata = """
summary @ A collection of utilities to access MS-DOS disks
homepage @ http://www.gnu.org/software/mtools/
license @ GPL-2
src_url @ http://ftp.gnu.org/gnu/mtools/$fullname.tar.bz2
arch @ ~x86_64
"""

def prepare():
    sed("-i '/^SAMPLE FILE$/s:^:# :' mtools.conf")

def install():
    raw_install("-j1 DESTDIR=%s" % install_dir)
    insfile("mtools.conf", "/etc/mtools.conf")
