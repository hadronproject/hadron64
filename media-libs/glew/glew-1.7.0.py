metadata = """
summary @ The OpenGL Extension Wrangler Library
homepage @ http://glew.sourceforge.net
license @ BSD MIT GPL
src_url @ http://downloads.sourceforge.net/$name/$fullname.tgz
arch @ ~x86
"""

depends = """
runtime @ x11-libs/libXmu x11-libs/libXi media-libs/mesa
"""

def prepare():
    sed("-i 's|lib64|lib|' config/Makefile.linux")

def install():
    raw_install('GLEW_DEST="%s/usr"' % install_dir)
    insdoc("LICENSE.txt")
    rmfile("/usr/lib/libGLEW.a")
    setmod("0755 %s/usr/lib/libGLEW*.so.%s" % (install_dir, version))
