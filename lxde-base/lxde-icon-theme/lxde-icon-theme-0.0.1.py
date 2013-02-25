metadata = """
summary @ LXDE default icon theme based on nuoveXT2
homepage @ http://lxde.org
license @ GPL
src_url @ http://downloads.sourceforge.net/lxde/$fullname.tar.bz2
arch @ ~x86_64
"""

get("main/gnome2_utils")

def install():
    raw_install("DESTDIR=%s" % install_dir)

def post_install():
    gnome2_icon_cache_update(target="/usr/share/icons/nuoveXT2")
