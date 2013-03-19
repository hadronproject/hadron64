metadata = """
summary @ Provides functionality for small OpenGL programs
homepage @ http://freeglut.sourceforge.net/
license @ MIT
src_url @ http://downloads.sourceforge.net/freeglut/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc x11-libs/libXxf86vm media-libs/mesa x11-libs/libXi media-libs/glu
"""

def prepare():
    sed('-i "s/smooth_opengl3 //" progs/demos/Makefile.*')

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
