metadata = """
summary @ The OpenGL Utility Library
homepage @ http://cgit.freedesktop.org/mesa/glu/
license @ LGPL
src_url @ ftp://ftp.freedesktop.org/pub/mesa/$name/$name-$version.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ media-libs/mesa
"""

def install():
    raw_install('DESTDIR=%s' % install_dir)
