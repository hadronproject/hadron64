metadata = """
summary @ GNOME default icon themes
homepage @ http://www.gnome.org
license @ LGPL3 CCPL-Attribution-ShareAlike-3.0
src_url @ http://ftp.gnome.org/pub/gnome/sources/$name/3.0/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ x11-themes/hicolor-icon-theme x11-misc/icon-naming-utils x11-libs/gtk+:2 
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)

def post_install():
    system("gtk-update-icon-cache -q -t -f /usr/share/icons/gnome")
