metadata = """
summary @ Miscellaneous procfs tools
homepage @ http://psmisc.sourceforge.net/index.html
license @ GPL-2
src_url @ http://downloads.sourceforge.net/psmisc/$fullname.tar.gz
arch @ ~x86
"""

def install():
    raw_install("DESTDIR=%s install" % install_dir)
    move("%s/usr/bin/killall" % install_dir, "/bin/killall")
    move("%s/usr/bin/fuser" % install_dir, "/bin/fuser")
