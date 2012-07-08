metadata = """
summary @ GNU database library
homepage @ http://www.gnu.org/software/gdbm/gdbm.html
license @ GPL-2
src_url @ ftp://ftp.gnu.org/gnu/$name/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
"""

def prepare():
    patch(level=1)

def configure():
    conf("--enable-libgdbm-compat --disable-static")

def install():
    linstall()
    makedirs("/usr/include/gdbm")
    makesym("../ndbm.h", "/usr/include/gdbm/ndbm.h")
    makesym("../gdbm.h", "/usr/include/gdbm/gdbm.h")
    makesym("../dbm.h", "/usr/include/gdbm/dbm.h")
