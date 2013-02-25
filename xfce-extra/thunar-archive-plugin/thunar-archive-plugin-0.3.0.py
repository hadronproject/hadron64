metadata = """
summary @ Thunar's archive plug-in
homepage @ http://goodies.xfce.org/projects/thunar-plugins/thunar-archive-plugin
license @ LGPL-2
src_url @ http://archive.xfce.org/src/thunar-plugins/$name/0.3/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ >=xfce-base/libxfce4util-4.8 >=xfce-base/exo-0.6 >=xfce-base/thunar-1.2
"""

get("main/gnome2_utils")

def configure():
    raw_configure("--prefix=/usr",
        "--sysconfdir=/etc",
        "--libexecdir=/usr/lib/xfce4",
        "--localstatedir=/var",
        "--disable-static")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("AUTHORS", "ChangeLog", "NEWS", "README", "THANKS")

def post_install():
    gnome2_icon_cache_update()
