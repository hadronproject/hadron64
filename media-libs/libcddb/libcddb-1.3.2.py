metadata = """
summary @ Library that implements the different protocols (CDDBP, HTTP, SMTP) to access data on a CDDB server (e.g. http://freedb.org).
homepage @ http://sourceforge.net/projects/libcddb/
license @ LGPL
src_url @ http://downloads.sourceforge.net/sourceforge/$name/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("AUTHORS", "ChangeLog", "NEWS", "README", "THANKS", "TODO")
