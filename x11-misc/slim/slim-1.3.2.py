metadata = """
summary @ Desktop-independent graphical login manager for X11
homepage @ http://slim.berlios.de/
license @ GPL2
src_url @ http://download.berlios.de/$name/$name-$version.tar.gz
arch @ ~x86_64
options @ pam
"""

depends = """
runtime @ x11-libs/libXmu x11-libs/libX11 x11-libs/libXpm x11-libs/libXft
media-libs/libpng:1.2 media-libs/jpeg
build @ dev-util/pkg-config x11-proto/xproto
"""

opt_runtime = """
pam @ sys-libs/pam
"""

def prepare():
#    sed("-i -e 's/png12/png14/g' Makefile")
# WTF ArchLinux ?
    patch(level=1)

def build():
    if opt("pam"):
        make("USE_PAM=1")
    else:
        make()

def install():
    raw_install("DESTDIR=%s MANDIR=/usr/share/man" % install_dir)
    insexe("%s/rc.d" % filesdir, "/etc/rc.d/slim")
    insfile("%s/logrotate" % filesdir, "/etc/logrotate.d/slim")
    if opt("pam"):
        insfile("%s/pam.d" % filesdir, "/etc/pam.d/slim")

    sed("-i 's|#xserver_arguments.*|xserver_arguments -nolisten tcp vt07|' %s/etc/slim.conf" % install_dir)
    sed("-i 's|/var/run/slim.lock|/var/lock/slim.lock|' %s/etc/slim.conf" % install_dir)

def post_install():
    warn("** Don't forget to add 'slim' to DAEMONS line in rc.conf ** ")
    if not opt("pam"):
        warn("** By the way, SLIM installed without PAM support ** ")
