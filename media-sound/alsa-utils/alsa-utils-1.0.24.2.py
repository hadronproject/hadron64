metadata = """
summary @ An alternative implementation of Linux sound support
homepage @ http://www.alsa-project.org
license @ GPL
src_url @ ftp://ftp.alsa-project.org/pub/utils/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ media-libs/alsa-lib dev-util/dialog sys-apps/pciutils sys-libs/ncurses sys-process/psmisc
build @ app-text/xmlto
"""

def prepare():
	patch(level=1)

def configure():
	conf(
	"--prefix=/usr --disable-xmlto")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insexe("%s/alsa" % filesdir, "/etc/rc.d/alsa")
    system("mkdir -p %s/etc/conf.d" % install_dir)
    system("mkdir -p %s/etc/pm/sleep.d" % install_dir)
    insfile("%s/alsa.conf.d" % filesdir, "/etc/conf.d/alsa")
    insfile("%s/90alsa" % filesdir, "/etc/pm/sleep.d/90alsa")
