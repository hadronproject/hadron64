metadata = """
summary @ Monitor configuration tool (part of LXDE)
homepage @ http://lxde.org/
license @ GPL-2
src_url @ http://downloads.sourceforge.net/sourceforge/lxde/$fullname.tar.gz
arch @ ~x86_64
"""

#FIXME: slot needed for gtk+

depends = """
commons @ x11-libs/gtk+:2 
x11-libs/libXrandr
x11-apps/xrandr
build @ x11-proto/randrproto
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)
