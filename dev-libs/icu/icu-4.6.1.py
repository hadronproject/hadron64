metadata = """
summary @ International Components for Unicode library
homepage @ http://www.icu-project.org
license @ icu
src_url @ http://download.icu-project.org/files/icu4c/4.6/icu4c-4_6-src.tgz
arch @ ~x86
"""

srcdir = name+"/source"

depends = """
runtime @ sys-devel/gcc
"""

def install():
    raw_install("-j1 DESTDIR=%s" % install_dir)