metadata = """
summary @ Desktop-independent graphical login manager for X11
homepage @ http://slim.berlios.de/
license @ GPL2
src_url @ http://download.berlios.de/$name/$name-$version.tar.gz
arch @ ~x86_64
options @ pam
"""

#FIXME: SLIM gives 'Failed to execute login command' error

depends = """
runtime @ x11-libs/libXmu x11-libs/libX11 x11-libs/libXpm x11-libs/libXft
media-libs/libpng media-libs/jpeg
build @ dev-util/pkg-config x11-proto/xproto
"""

opt_runtime = """
pam @ sys-libs/pam
"""

get("cmake_utils")

#To fix a compilation error related with libXmu
export('LDFLAGS', '-lXmu')

def prepare():
    sed("-i 's|usr/lib/systemd/system|/&|' CMakeLists.txt")

def configure():
    if opt("pam"):
        myconf = '-DUSE_PAM=yes'
    else:
        myconf = '-DUSE_PAM=no'

    cmake_conf("-DCMAKE_BUILD_TYPE=Release \
                -DUSE_CONSOLEKIT=no \
                %s" % myconf)
        
def install():
    raw_install("DESTDIR=%s MANDIR=/usr/share/man" % install_dir)
    insfile("%s/logrotate" % filesdir, "/etc/logrotate.d/slim")
    if opt("pam"):
        insfile("%s/pam.d" % filesdir, "/etc/pam.d/slim")

    sed("-i 's|#xserver_arguments.*|xserver_arguments -nolisten tcp vt07|' %s/etc/slim.conf" % install_dir)
    sed("-i 's|/var/run/slim.lock|/var/lock/slim.lock|' %s/etc/slim.conf" % install_dir)

def post_install():
    warn("** Do not forget to type 'systemctl enable slim' in order to \
    start SLIM on startup ** ")
    if not opt("pam"):
        warn("** By the way, SLIM installed without PAM support ** ")
