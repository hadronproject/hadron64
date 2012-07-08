metadata = """
summary @ Configuration tools for Linux networking
homepage @ http://www.tazenda.demon.co.uk/phil/net-tools
license @ GPL
src_url @ http://www.tazenda.demon.co.uk/phil/$name/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
common @ sys-libs/glibc
"""

standard_procedure = False

def prepare():
    patch(level=1)

def build():
    system('yes "" | make')

def install():
    system("make BASEDIR=%s update" % install_dir)
