metadata = """
summary @ The ultimate lightweight window manager
homepage @ http://www.jfc.org.uk/software/lwm.html
license @ GPL-2
src_url @ http://www.jfc.org.uk/files/lwm/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/libX11 x11-libs/libXext x11-libs/libSM x11-libs/libICE
build @ x11-proto/xextproto x11-proto/xproto x11-misc/imake
"""

def prepare():
    sed("""-i -e "s/(SMLIB)/& -lICE/g" Imakefile""")
    system("xmkmf")

def build():
    make()

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("AUTHORS", "BUGS", "ChangeLog")
