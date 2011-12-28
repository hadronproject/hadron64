metadata = """
summary @ GNU database library
homepage @ http://www.gnu.org/software/gdbm/gdbm.html
license @ GPL-2
src_url @ ftp://ftp.gnu.org/gnu/$name/$fullname.tar.gz
arch @ ~x86
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
    if isexists("/usr/include/gdbm/ndbm.h"):
        rmfile("/usr/include/gdbm/ndbm.h")
    makesym("../ndbm.h", "/usr/include/gdbm/ndbm.h")
    
    if isexists("/usr/include/gdbm/gdbm.h"):
        rmfile("/usr/include/gdbm/gdbm.h")
    makesym("../gdbm.h", "/usr/include/gdbm/gdbm.h")

    if isexists("/usr/include/gdbm/dbm.h"):
        rmfile("/usr/include/gdbm/dbm.h")
    makesym("../dbm.h", "/usr/include/gdbm/dbm.h")
