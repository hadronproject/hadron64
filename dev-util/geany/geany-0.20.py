metadata = """
summary @ GTK+ based fast and lightweight IDE
homepage @ http://geany.org
license @ GPL-2
src_url @ http://download.geany.org/$name-$version.tar.bz2
options @ vte
"""

def configure():
    conf(config_enable("vte"))
