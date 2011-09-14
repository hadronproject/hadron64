metadata = """
summary @ Common files of the LXDE Desktop
homepage @ http://lxde.org/
license @ GPL-2
src_url @ http://downloads.sourceforge.net/lxde/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ x11-libs/libX11 sys-libs/glib lxde-base/lxde-icon-theme
build @ sys-devel/automake
"""

get("main/gnome2_utils")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insfile("lxde-logout.desktop", 
            "/usr/share/applications/lxde-logout.desktop")

def post_install():
    gnome2_icon_cache_update(target="/usr/share/icons/nuoveXT2")
