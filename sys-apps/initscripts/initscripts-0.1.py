metadata = """
summary @ System initialization/bootup scripts
homepage @ http://hadronproject.org
license @ GPL-3
src_url @ http://hadronproject.org/distfiles/initscripts/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-apps/baselayout sys-fs/udev
"""

standart_procedure = False

srcdir = "initscripts"

def install():
    system("DESTDIR=%s ./install.sh" % install_dir)
