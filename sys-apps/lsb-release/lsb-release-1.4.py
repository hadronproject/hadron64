metadata = """
summary @ LSB version query program
homepage @ http://www.linuxbase.org/
license @ GPL2
src_url @ http://downloads.sourceforge.net/lsb/$fullname.tar.gz
arch @ ~x86_64
"""

def install():
    linstall()

    insfile("%s/lsb-release" % filesdir, "/etc/lsb-release")
    #makedirs("/etc")
    #touch("/etc/lsb-release")
    #system('echo "DISTRIB_DESCRIPTION=\"Hadron GNU/Linux\"" > "%s/etc/lsb-release"' % install_dir)
