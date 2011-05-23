metadata = """
summary @ GTK+ based fast and lightweight IDE
homepage @ http://geany.org
license @ GPL-2
src_url @ http://download.geany.org/$name-$version.tar.bz2
options @ vte
"""

depend =  """
runtime @ x11-libs/gtk+  dev-libs/glib x11-libs/vte
builr @ dev-util/pkg-config dev-util/intltool
"""

def configure():
    conf(config_enable("vte"))

def install():
    raw_install("DESTDIR=%s" % install_dir)

def post_install():
    system("gtk-update-icon-cache -q -t -f /usr/share/icons/hicolor")
