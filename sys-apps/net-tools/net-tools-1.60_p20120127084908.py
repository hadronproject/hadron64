metadata = """
summary @ Configuration tools for Linux networking
homepage @ http://www.tazenda.demon.co.uk/phil/net-tools
license @ GPL-2
src_url @ http://distfiles.gentoo.org/distfiles/net-tools-1.60_p20120127084908.tar.xz
arch @ ~x86_64
"""

depends = """
common @ sys-libs/glibc
"""

standard_procedure = False

def prepare():
    sed("-i -e '/Token/s/y$/n/' -e '/STRIP/s/y$/n/' config.in")
    patch(level=1)

def configure():
    if not system('yes "" | ./configure.sh config.in'):
        terminate()

def build():
    if not system('yes "" | make'):
        terminate()

def install():
    raw_install("BASEDIR=%s update" % install_dir)
