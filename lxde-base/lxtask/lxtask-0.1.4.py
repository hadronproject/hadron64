metadata = """
summary @ Task manager of the LXDE Desktop
homepage @ http://lxde.org/
license @ GPL-2
src_url @ http://downloads.sourceforge.net/sourceforge/lxde/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/gtk+:2 
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)
