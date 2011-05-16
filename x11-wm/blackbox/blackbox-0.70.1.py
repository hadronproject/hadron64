metadata = """
summary @ A window manager for X11
homepage @ http://blackboxwm.sourceforge.net/
license @ MIT
src_url @ http://downloads.sourceforge.net/blackboxwm/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc x11-libs/libXft x11-libs/libXext x11-libs/libX11
"""

def prepare():
    patch("gcc4.3.patch", level=1)
    patch("bbdock.patch")
    patch("bsetbg-feh.patch")
    patch("textpropertytostring-unconditional.patch", level=1)

def install():
    raw_install("DESTDIR=%s" % install_dir)
    
    insdoc("LICENSE")
