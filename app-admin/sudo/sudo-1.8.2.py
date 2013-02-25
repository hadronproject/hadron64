metadata = """
summary @ Give certain users the ability to run some commands as root
homepage @ http://www.sudo.ws/sudo/
license @ as-is BSD
src_url @ ftp://ftp.sudo.ws/pub/sudo/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc sys-libs/pam
"""

reserve_files = ['/etc/sudoers', '/etc/pam.d/sudo']

def configure():
    conf("--with-pam",
            "--with-env-editor", 
            "--with-all-insults", 
            "--with-logfac=auth")

def install():
    makedirs("/var/lib")

    raw_install("DESTDIR=%s" % install_dir)

    insfile("%s/sudo.pam" % filesdir, "/etc/pam.d/sudo")

    insfile("doc/LICENSE", "/usr/share/licenses/sudo/LICENSE")
