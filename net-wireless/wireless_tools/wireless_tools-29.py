metadata = """
summary @ A collection of tools to configure IEEE 802.11 wireless LAN cards
homepage @ http://www.hpl.hp.com/personal/Jean_Tourrilhes/Linux/Tools.html
license @ GPL
src_url @ http://www.hpl.hp.com/personal/Jean_Tourrilhes/Linux/$name.$version.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc
"""

srcdir = name+"."+version

def prepare():
    patch()

def install():
    raw_install('PREFIX=%s/usr \
            INSTALL_DIR="%s/usr/sbin" \
            INSTALL_LIB="%s/usr/lib" \
            INSTALL_INC="%s/usr/include" \
            INSTALL_MAN="%s/usr/share/man"' % ((install_dir,)*5))
