metadata = """
summary @ A commandline option parser
homepage @ http://rpm5.org/
license @ custom
src_url @ http://rpm5.org/files/$name/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc
"""

# FIXME: add options  

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("COPYING")
