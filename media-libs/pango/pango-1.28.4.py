metadata = """
summary @ A library for layout and rendering of text
homepage @ http://www.pango.org/
license @ LGPL
src_url @ http://ftp.gnome.org/pub/gnome/sources/pango/1.28/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glib x11-libs/cairo x11-libs/libXft dev-libs/libthai 
          media-libs/freetype

build @ x11-libs/libXt
"""

def configure():
    conf("--with-included-modules=basic-fc")

def build():
    export("HOME", build_dir)
    make()

def install():
	export("HOME", build_dir)
	raw_install("DESTDIR=%s" % install_dir)

def post_install():
    system("/sbin/ldconfig -r / &>/dev/null")

    # create pango.modules
    if isfile("/etc/pango/pango.modules"):
        rmfile("/etc/pango/pango.modules")
    system("/usr/bin/pango-querymodules > /etc/pango/pango.modules")
