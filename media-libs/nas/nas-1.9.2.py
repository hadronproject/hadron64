metadata = """
summary @ Network Audio System is a network transparent, client/server audio transport system
homepage @ http://radscan.com/nas.html
license @ custom
src_url @ http://downloads.sourceforge.net/sourceforge/$name/$name-$version.src.tar.gz
arch @ ~x86
"""

depends = """
runtime @ x11-libs/libXt x11-libs/libXau x11-libs/libXaw x11-libs/libX11 x11-libs/libXres
build @ x11-misc/imake x11-proto/xproto x11-misc/gccmakedep
"""

standard_procedure = False

def build():
    system("xmkmf")
    make("World")

def install():
    raw_install("DESTDIR=%s USRLIBDIR=/usr/lib" % install_dir)
    insdoc("BUILDNOTES", "FAQ", "HISTORY", "README", "RELEASE", "TODO")

#ERROR
