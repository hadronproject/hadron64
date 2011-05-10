metadata = """
summary @ X.Org initialisation program
homepage @ http://xorg.freedesktop.org/ 
license @ custom
src_url @ http://xorg.freedesktop.org/archive/individual/app/xinit-$version.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ x11-libs/libX11 x11-misc/xauth
"""

#srcdir = "xinit-%s" % version

def prepare():
    patch("06_move_serverauthfile_into_tmp.diff", level=1)

def configure():
    conf("--with-xinitdir=/etc/X11/xinit")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    
    insdoc("COPYING")

