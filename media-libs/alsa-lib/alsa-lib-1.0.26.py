metadata = """
summary @ An alternative implementation of Linux sound support
homepage @ http://www.alsa-project.org/
license @ GPL-2
src_url @ ftp://ftp.alsa-project.org/pub/lib/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
build @ dev-lang/python:2.7
"""

def configure():
    conf('--with-pythonlibs="-lpthread -lm -ldl -lpython2.7"',
            '--with-pythonincludes=-I/usr/include/python2.7')

def install():
    raw_install("DESTDIR=%s" % install_dir)
