metadata = """
summary @ GTK+ based fast and lightweight IDE
homepage @ http://geany.org
license @ GPL-2
src_url @ http://download.geany.org/$name-$version.tar.bz2
arch @ ~x86_64
options @ vte
"""

depends = """
runtime @ x11-libs/gtk+:2 sys-libs/glib
build @ dev-util/pkg-config dev-util/intltool
"""

opt_runtime = """
vte @ x11-libs/vte
"""
get("gnome2_utils")

def configure():
    conf(config_enable("vte"))

def install():
    raw_install("DESTDIR=%s" % install_dir)

def post_install():
    gnome2_icon_cache_update()

