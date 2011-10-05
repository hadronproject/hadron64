metadata = """
summary @ LXDE keyboard and mouse configuration tool
homepage @ http://lxde.sourceforge.net/
license @ GPL-2
src_url @ http://downloads.sourceforge.net/lxde/$fullname.tar.gz
arch @ ~x86
"""

# FIXME: gtk+ slot needed!

depends = """
commons @ sys-libs/glib x11-libs/gtk+:2 
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("AUTHORS", "README")
