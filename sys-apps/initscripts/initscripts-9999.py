metadata = """
summary @ System initialization/bootup scripts
homepage @ http://hadronproject.org
license @ GPL-3
arch @ ~x86
"""

depends = """
runtime @ sys-apps/baselayout sys-fs/udev
"""

standard_procedure = False

#srcdir = "initscripts"

def prepare():
    remote = "git://gitorious.org/hadron/initscripts.git"
    notify("cloning %s" % remote)
    system("git clone %s" % remote)

def install():
    cd("initscripts")
    raw_install("DESTDIR=%s" % install_dir)
    #system("DESTDIR=%s ./install.sh" % install_dir)
