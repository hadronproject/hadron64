metadata = """
summary @ A bootloader for Linux
homepage @ https://alioth.debian.org/projects/lilo/
license @ BSD
src_url @ http://lilo.alioth.debian.org/ftp/sources/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
build @ sys-devel/bin86 app-arch/sharutils
"""

def build():
    export("LC_ALL", "C")
    make("all")

def install():
    installd()

    insfile("%s/lilo.conf" % filesdir, "/etc/lilo.conf")
    insdoc("COPYING")
